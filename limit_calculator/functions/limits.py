# functions/limits.py
from sympy import symbols, limit, oo, pi, E, latex
from .math_functions import math_functions
from .continuity import is_continuous, find_discontinuities


def calculate_left_right_limit(expression: str, variable: str, point: float) -> tuple:
    """
    计算给定表达式在变量趋向于某一点时的左极限和右极限，并比较它们是否相等。

    参数:
        expression (str): 表达式字符串。
        variable (str): 自变量名称。
        point (int/float/symbols.oo): 趋向的点。

    返回:
        左极限、右极限以及它们是否相等的结果。
    """
    x = symbols(variable)

    try:
        # 计算左极限
        left_lim = limit(eval(expression, {
                         **math_functions, 'pi': pi, 'e': E, variable: x}), x, point, dir='-')
    except Exception as e:
        print(f"无法计算左极限: {e}")
        left_lim = "无法计算"

    try:
        # 计算右极限
        right_lim = limit(eval(expression, {
                          **math_functions, 'pi': pi, 'e': E, variable: x}), x, point, dir='+')
    except Exception as e:
        print(f"无法计算右极限: {e}")
        right_lim = "无法计算"

    # 比较左极限和右极限是否相等
    if left_lim != "无法计算" and right_lim != "无法计算":
        are_equal = left_lim == right_lim
    else:
        are_equal = False

    return left_lim, right_lim, are_equal


def calculate_overall_limit(expression: str, variable: str, point: float) -> float:
    """
    计算给定表达式在变量趋向于某一点时的整体极限。

    参数:
        expression (str): 表达式字符串。
        variable (str): 自变量名称。
        point (float): 趋向的点。

    返回:
        整体极限或 None 如果无法计算。
    """
    x = symbols(variable)

    try:
        # 计算整体极限
        overall_limit = limit(
            eval(expression, {**math_functions, 'pi': pi, 'e': E, variable: x}), x, point)
    except Exception as e:
        print(f"无法计算整体极限: {e}")
        overall_limit = None

    return overall_limit


def check_continuity_and_discontinuities(expression: str, variable: str, point: float, interval: tuple) -> tuple:
    """
    检查给定表达式在某一点的连续性，并查找指定区间内的间断点。

    参数:
        expression (str): 表达式字符串。
        variable (str): 自变量名称。
        point (float): 趋向的点。
        interval (tuple): 检查的区间 (start, end)。

    返回:
        连续性结果和间断点列表。
    """
    continuous = is_continuous(expression, variable, point)
    discontinuities = find_discontinuities(expression, variable, interval)
    return continuous, discontinuities
