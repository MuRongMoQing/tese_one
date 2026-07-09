# functions/continuity.py
from sympy import symbols, limit, oo, pi, E, latex, sympify


def is_continuous(expression: str, variable: str, point: float) -> bool:
    """
    判断给定表达式在某一点是否连续。

    参数:
        expression (str): 表达式字符串。
        variable (str): 自变量名称。
        point (float): 趋向的点。

    返回:
        是否连续（True 或 False）。
    """
    x = symbols(variable)
    expr = sympify(expression)

    try:
        left_lim = limit(expr, x, point, dir='-')
        right_lim = limit(expr, x, point, dir='+')
        value_at_point = expr.subs(x, point)

        return left_lim == right_lim == value_at_point
    except Exception as e:
        print(f"无法计算连续性: {e}")
        return False


def find_discontinuities(expression: str, variable: str, interval: tuple, step: float = 0.1) -> list:
    """
    查找给定表达式在指定区间内的间断点。

    参数:
        expression (str): 表达式字符串。
        variable (str): 自变量名称。
        interval (tuple): 检查的区间 (start, end)。
        step (float): 步长，默认为 0.1。

    返回:
        间断点列表。
    """
    x = symbols(variable)
    x = symbols(variable)
    expr = sympify(expression)
    discontinuities = []

    for point in [round(interval[0] + i * step, 5) for i in range(int((interval[1] - interval[0]) / step) + 1)]:
        if not is_continuous(expression, variable, point):
            discontinuities.append(point)

    # 特别处理 tan(x) 在 pi/2 + k*pi 处的不连续性
    if 'tan' in expression:
        for k in range(int(interval[0] / pi), int(interval[1] / pi) + 1):
            discontinuity_point = (k + 0.5) * pi
            if interval[0] <= discontinuity_point <= interval[1]:
                discontinuities.append(discontinuity_point)

    return discontinuities
