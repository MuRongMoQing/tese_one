import tkinter as tk


class ResultDisplay(tk.Label):
    def __init__(self, master: tk.Tk) -> None:
        """
        初始化结果标签。

        参数:
            master (tk.Tk): Tkinter 的主窗口。
        """
        super().__init__(master, text="", justify=tk.LEFT)

    def set_text(self, text: str) -> None:
        """
        更新结果标签的文本内容。

        参数:
            text (str): 要显示的文本。
        """
        self.config(text=text)
