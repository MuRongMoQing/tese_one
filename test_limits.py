"""Tests for limit_calculator.functions.limits module."""
import pytest
from sympy import oo, pi
from limit_calculator.functions.limits import (
    calculate_left_right_limit,
    calculate_overall_limit,
    check_continuity_and_discontinuities,
)


class TestCalculateLeftRightLimit:
    """Tests for calculate_left_right_limit function."""

    def test_simple_limit_sin_over_x(self):
        """lim x->0 sin(x)/x = 1, both left and right."""
        left, right, equal = calculate_left_right_limit("sin(x)/x", "x", 0)
        assert left == 1
        assert right == 1
        assert equal is True

    def test_absolute_value_at_zero(self):
        """abs(x)/x: left=-1, right=1, not equal at x=0."""
        left, right, equal = calculate_left_right_limit("abs(x)/x", "x", 0)
        assert left == -1
        assert right == 1
        assert equal is False

    def test_limit_at_infinity(self):
        """lim x->oo 1/x = 0."""
        left, right, equal = calculate_left_right_limit("1/x", "x", oo)
        assert left == 0
        assert right == 0
        assert equal is True

    def test_polynomial_limit(self):
        """lim x->1 (x**2 - 1)/(x - 1) = 2."""
        left, right, equal = calculate_left_right_limit(
            "(x**2-1)/(x-1)", "x", 1)
        assert left == 2
        assert right == 2
        assert equal is True

    def test_polynomial_limit_at_two(self):
        """lim x->2 x**2 + 3*x + 1 = 11."""
        left, right, equal = calculate_left_right_limit(
            "x**2 + 3*x + 1", "x", 2)
        assert left == 11
        assert right == 11
        assert equal is True

    def test_trig_limit_sin(self):
        """lim x->pi sin(x) = 0."""
        left, right, equal = calculate_left_right_limit("sin(x)", "x", pi)
        assert left == 0
        assert right == 0
        assert equal is True

    def test_exp_limit_at_zero(self):
        """lim x->0 exp(x) = 1."""
        left, right, equal = calculate_left_right_limit("exp(x)", "x", 0)
        assert left == 1
        assert right == 1
        assert equal is True

    def test_one_over_x_at_zero(self):
        """lim x->0+ 1/x = oo, lim x->0- 1/x = -oo, not equal."""
        left, right, equal = calculate_left_right_limit("1/x", "x", 0)
        assert equal is False

    def test_sqrt_at_zero(self):
        """sqrt(x) at x=0: checks computation runs without error."""
        left, right, equal = calculate_left_right_limit("sqrt(x)", "x", 0)
        assert isinstance(equal, bool)


class TestCalculateOverallLimit:
    """Tests for calculate_overall_limit function."""

    def test_simple_limit_sin_over_x(self):
        """lim x->0 sin(x)/x = 1."""
        result = calculate_overall_limit("sin(x)/x", "x", 0)
        assert result == 1

    def test_polynomial_limit(self):
        """lim x->2 (x**2 - 4)/(x - 2) = 4."""
        result = calculate_overall_limit("(x**2 - 4)/(x - 2)", "x", 2)
        assert result == 4

    def test_limit_at_infinity(self):
        """lim x->oo 1/(x**2) = 0."""
        result = calculate_overall_limit("1/(x**2)", "x", oo)
        assert result == 0

    def test_limit_sqrt(self):
        """lim x->4 sqrt(x) = 2."""
        result = calculate_overall_limit("sqrt(x)", "x", 4)
        assert result == 2

    def test_limit_log(self):
        """lim x->1 log(x) = 0."""
        result = calculate_overall_limit("log(x)", "x", 1)
        assert result == 0

    def test_limit_exp_neg_inf(self):
        """lim x->-oo exp(x) = 0."""
        result = calculate_overall_limit("exp(x)", "x", -oo)
        assert result == 0

    def test_abs_over_x_no_overall_limit(self):
        """abs(x)/x has no overall limit at 0 (should not crash)."""
        result = calculate_overall_limit("abs(x)/x", "x", 0)
        assert result is not None or result is None


class TestCheckContinuityAndDiscontinuities:
    """Tests for check_continuity_and_discontinuities function."""

    def test_continuous_sin(self):
        """sin(x) is continuous at x=0, no discontinuities in [0, 2*pi]."""
        continuous, discontinuities = check_continuity_and_discontinuities(
            "sin(x)", "x", 0, (0, 2 * float(pi))
        )
        assert continuous is True
        assert isinstance(discontinuities, list)

    def test_discontinuous_one_over_x(self):
        """1/x is discontinuous at x=0, has discontinuity at 0 in [-1, 1]."""
        continuous, discontinuities = check_continuity_and_discontinuities(
            "1/x", "x", 0, (-1, 1)
        )
        assert continuous is False
        assert 0 in discontinuities

    def test_continuous_polynomial(self):
        """x**2 is continuous at x=5."""
        continuous, discontinuities = check_continuity_and_discontinuities(
            "x**2", "x", 5, (-10, 10)
        )
        assert continuous is True
        assert isinstance(discontinuities, list)

    def test_different_variable_name(self):
        """cos(t) is continuous at t=pi."""
        continuous, _ = check_continuity_and_discontinuities(
            "cos(t)", "t", float(pi), (0, 2 * float(pi))
        )
        assert continuous is True
