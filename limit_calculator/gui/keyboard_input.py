# gui/keyboard_input.py
import tkinter as tk


def create_keyboard(master: tk.Tk, on_key_press) -> tk.Frame:
    """
    创建一个虚拟键盘，包含数字、运算符和其他常用符号，并绑定按键事件处理函数。

    参数:
        master (tk.Tk): Tkinter 的主窗口。
        on_key_press: 按键事件处理函数。

    返回:
        tk.Frame: 虚拟键盘的框架。
    """
    keyboard_frame = tk.Frame(master)

    keys = [
        ['7', '8', '9', '(', ')'],
        ['4', '5', '6', 'x', 'C'],
        ['1', '2', '3', 'pi', 'e'],
        ['0', '.', 'sin', 'cos', 'tan'],
        ['exp', 'log', 'sqrt']
    ]

    for row in keys:
        row_frame = tk.Frame(keyboard_frame)
        row_frame.pack(side=tk.TOP, fill=tk.X)
        for key in row:
            button = tk.Button(row_frame, text=key, width=5,
                               height=2, command=lambda k=key: on_key_press(k))
            button.pack(side=tk.LEFT, padx=5, pady=5)

    return keyboard_frame
