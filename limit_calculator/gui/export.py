# gui/export.py
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from matplotlib.font_manager import FontProperties

# 设置支持中文的字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体或其他支持中文的字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 注册中文字体
pdfmetrics.registerFont(TTFont('SimHei', 'SimHei.ttf'))  # 请确保 SimHei.ttf 在你的系统路径中

def export_to_image(result_text: str) -> None:
    """
    将结果文本导出为图片文件 `result.png`，并支持中文字符。

    参数:
        result_text (str): 要导出的结果文本。
    """
    # 打印调试信息
    print(f"Exporting text: {result_text}")

    plt.figure(figsize=(8, 6))
    plt.text(0.5, 0.5, result_text, fontsize=12, ha='center', va='center', wrap=True, usetex=True)
    plt.axis('off')
    plt.savefig("result.png", bbox_inches='tight')
    plt.close()
    print("结果已保存为图片: result.png")

def export_to_pdf(result_text: str) -> None:
    """
    将结果文本导出为 PDF 文件 `result.pdf`，并支持中文字符和多行文本。

    参数:
        result_text (str): 要导出的结果文本。
    """
    # 创建一个 PDF 文档模板
    doc = SimpleDocTemplate("result.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    custom_style = ParagraphStyle(name='Custom', fontName='SimHei', fontSize=12, leading=14)

    # 将 result_text 转换为段落
    paragraphs = [Paragraph(line, custom_style) for line in result_text.split('\n')]

    # 构建文档内容
    doc.build(paragraphs)
    print("结果已保存为PDF: result.pdf")