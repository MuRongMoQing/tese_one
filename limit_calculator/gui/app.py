# gui/app.py
import tkinter as tk
from tkinter import messagebox
from sympy import latex, pi, E, symbols, sqrt, sympify
from .keyboard_input import create_keyboard
from .result_display import ResultDisplay
from ..functions.limits import calculate_left_right_limit, calculate_overall_limit, check_continuity_and_discontinuities
from .export import export_to_image, export_to_pdf


class LimitCalculatorApp:
    def __init__(self, master: tk.Tk) -> None:
        """
        初始化极限计算器应用程序。

        参数:
            master (tk.Tk): Tkinter 的主窗口。
        """
        self.master = master
        master.title("极限计算器")
        master.geometry("500x600")  # 初始窗口大小
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        # 创建标签和输入框
        self.create_widgets()

        # 创建虚拟键盘
        self.keyboard_frame = create_keyboard(self.master, self.on_key_press)
        self.keyboard_frame.grid(
            row=10, column=0, columnspan=2, pady=10, sticky='nsew')

        # 绑定焦点事件
        self.entry_expression.bind("<FocusIn>", self.on_focus_in)
        self.entry_variable.bind("<FocusIn>", self.on_focus_in)
        self.entry_point.bind("<FocusIn>", self.on_focus_in)
        self.entry_interval_start.bind("<FocusIn>", self.on_focus_in)
        self.entry_interval_end.bind("<FocusIn>", self.on_focus_in)

        self.current_entry = self.entry_expression  # 默认选中函数表达式输入框

    def create_widgets(self) -> None:
        """
        创建应用程序的用户界面组件，包括标签、输入框、按钮等。
        """
        # 函数表达式
        tk.Label(self.master, text="函数表达式:").grid(
            row=0, column=0, padx=5, pady=5, sticky='w')
        self.entry_expression = tk.Entry(self.master, width=40)
        self.entry_expression.grid(
            row=0, column=1, padx=5, pady=5, sticky='ew')

        # 自变量
        tk.Label(self.master, text="自变量:").grid(
            row=1, column=0, padx=5, pady=5, sticky='w')
        self.entry_variable = tk.Entry(self.master, width=40)
        self.entry_variable.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

        # 目标点
        tk.Label(self.master, text="目标点:").grid(
            row=2, column=0, padx=5, pady=5, sticky='w')
        self.entry_point = tk.Entry(self.master, width=40)
        self.entry_point.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

        # 区间
        tk.Label(self.master, text="区间 (start, end):").grid(
            row=3, column=0, padx=5, pady=5, sticky='w')
        self.entry_interval_start = tk.Entry(self.master, width=20)
        self.entry_interval_start.grid(
            row=3, column=1, padx=5, pady=5, sticky='w')
        self.entry_interval_end = tk.Entry(self.master, width=20)
        self.entry_interval_end.grid(
            row=3, column=1, padx=5, pady=5, sticky='e')

        # 计算按钮
        calculate_button = tk.Button(
            self.master, text="计算", command=self.on_calculate)
        calculate_button.grid(
            row=4, column=0, columnspan=2, pady=10, sticky='ew')

        # 导出按钮
        export_button = tk.Button(
            self.master, text="导出结果", command=self.on_export)
        export_button.grid(row=6, column=0, columnspan=2, pady=10, sticky='ew')

        # 结果标签
        self.result_display = ResultDisplay(self.master)
        self.result_display.grid(
            row=5, column=0, columnspan=2, pady=10, sticky='ew')

    def on_focus_in(self, event: tk.Event) -> None:
        """
        当输入框获得焦点时，更新当前选中的输入框。

        参数:
            event (tk.Event): Tkinter 事件对象。
        """
        self.current_entry = event.widget

    def on_calculate(self) -> None:
        """
        计算表达式的左极限、右极限和整体极限，并在结果标签中显示。
        """
        expression = self.entry_expression.get()
        variable = self.entry_variable.get()
        point_str = self.entry_point.get()
        interval_start = self.entry_interval_start.get()
        interval_end = self.entry_interval_end.get()

        try:
            if point_str.lower() == 'inf':
                point = float('inf')
            elif point_str.lower() == '-inf':
                point = float('-inf')
            elif 'pi' in point_str or 'e' in point_str:
                point = eval(
                    point_str, {'pi': pi, 'e': E, variable: symbols(variable)})
            else:
                point = float(point_str)
        except ValueError:
            self.result_display.set_text("请输入有效的点")
            return

        try:
            interval = (eval(interval_start, {'pi': pi, 'e': E}), eval(
                interval_end, {'pi': pi, 'e': E}))
        except ValueError:
            self.result_display.set_text("请输入有效的区间")
            return

        left_lim, right_lim, are_equal = calculate_left_right_limit(
            expression, variable, point)
        overall_limit = calculate_overall_limit(expression, variable, point)
        continuous, discontinuities = check_continuity_and_discontinuities(
            expression, variable, point, interval)

        result_text = f"左极限: ${latex(left_lim)}$\n右极限: ${latex(right_lim)}\n"
        if are_equal:
            result_text += "左极限和右极限相等\n"
            if overall_limit is not None:
                result_text += f"整体极限: ${latex(overall_limit)}$\n"
            else:
                result_text += "无法计算整体极限\n"
        else:
            result_text += "左极限和右极限不相等\n"
            result_text += "函数在该点没有极限\n"

        if continuous:
            result_text += "函数在该点是连续的\n"
        else:
            result_text += "函数在该点是不连续的\n"

        if discontinuities:
            result_text += f"区间 {interval} 内的间断点: {discontinuities}\n"
        else:
            result_text += "区间内没有间断点\n"

        self.result_display.set_text(result_text)

    def on_key_press(self, key: str) -> None:
        """
        处理虚拟键盘按键事件，将相应的字符插入到当前选中的输入框中。

        参数:
            key (str): 按下的键。
        """
        if key == 'C':
            self.current_entry.delete(0, tk.END)
        elif key in ['sin', 'cos', 'tan', 'exp', 'log']:
            self.current_entry.insert(tk.END, f"{key}(")
        elif key == 'sqrt':
            self.current_entry.insert(tk.END, "sqrt(")
        elif key in ['pi', 'e', 'x', '(', ')']:
            self.current_entry.insert(tk.END, key)
        else:
            self.current_entry.insert(tk.END, key)

    def on_export(self) -> None:
        """
        导出计算结果为图片或 PDF 格式。
        """
        result_text = self.result_display.cget("text")
        if result_text:
            export_format = messagebox.askquestion(
                "导出格式", "请选择导出格式:\n是 - 图片\n否 - PDF")
            if export_format == 'yes':
                export_to_image(result_text)
            else:
                export_to_pdf(result_text)
        else:
            messagebox.showwarning("导出失败", "没有结果可以导出")
