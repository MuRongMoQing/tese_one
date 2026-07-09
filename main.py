import tkinter as tk
from limit_calculator.gui.app import LimitCalculatorApp

def main() -> None:
    """
    项目的入口函数，启动极限计算器应用程序。
    """
    root = tk.Tk()
    app = LimitCalculatorApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()