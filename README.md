# 极限计算器

## 项目结构

PythonProject1  
├── .venv  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── Lib  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── Scripts  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── share  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── CACHEDIR.TAG  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── pyvenv.cfg  
├── limit_calculator  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── __init__.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── functions  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── __init__.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── limits.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── continuity.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── math_functions.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── gui  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── __init__.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── app.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── export.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── keyboard_input.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── result_display.py  
├── main.py  
├── README.md  
└── .gitignore  

## 功能

- **计算极限**: 计算给定表达式在某一点的左极限、右极限和整体极限。
- **判断连续性**: 判断给定表达式在某一点是否连续。
- **查找间断点**: 查找给定表达式在指定区间内的间断点。
- **导出结果**: 将计算结果导出为图片或 PDF 格式。
- **临时存储与清理**: 自动存储计算过程中的临时数据，并在程序关闭时自动清理。

## 使用方法

1. 运行 `main.py` 启动应用程序。
2. 在应用程序界面中输入表达式、自变量、目标点和区间。
3. 点击“计算”按钮查看结果。
4. 点击“导出结果”按钮选择导出格式并保存结果。

## 依赖

- `matplotlib`
- `reportlab`
- `sympy`
- `tkinter`

## 示例

python  
示例表达式: sin(x) / x  
自变量: x  
目标点: 0  
区间: (-1, 1)  
运行上述示例，程序将计算表达式在目标点的极限，并判断其连续性及查找区间内的间断点。