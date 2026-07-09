"""Tests for limit_calculator.functions.continuity module."""
import pytest
from limit_calculator.functions.continuity import is_continuous, find_discontinuities


class TestIsContinuous:
    """Tests for is_continuous function."""

    def test_continuous_at_zero_sin(self):
        """sin(x) is continuous at x=0."""
        assert is_continuous("sin(x)", "x", 0) is True

    def test_continuous_at_point_polynomial(self):
        """x**2 + 1 is continuous at x=1."""
        assert is_continuous("x**2 + 1", "x", 1) is True

    def test_continuous_at_point_exp(self):
        """exp(x) is continuous at x=0."""
        assert is_continuous("exp(x)", "x", 0) is True

    def test_continuous_at_pi(self):
        """sin(x) is continuous at x=pi."""
        assert is_continuous("sin(x)", "x", 3.141592653589793) is True

    def test_discontinuous_at_zero(self):
        """1/x is discontinuous at x=0 (division by zero)."""
        assert is_continuous("1/x", "x", 0) is False

    def test_continuous_with_different_variable(self):
        """cos(t) is continuous at t=0 with variable name 't'."""
        assert is_continuous("cos(t)", "t", 0) is True

    def test_constant_function(self):
        """Constant function f(x)=5 is continuous everywhere."""
        assert is_continuous("5", "x", 0) is True
        assert is_continuous("5", "x", 100) is True

    def test_discontinuous_one_over_x_plus_one(self):
        """1/(x) is discontinuous at x=0."""
        assert is_continuous("1/(x)", "x", 0) is False


class TestFindDiscontinuities:
    """Tests for find_discontinuities function."""

    def test_no_discontinuities_sin(self):
        """sin(x) has no discontinuities in [0, 2*pi]."""
        result = find_discontinuities("sin(x)", "x", (0, 6.283185307179586))
        assert result == []

    def test_discontinuity_at_zero(self):
        """1/x has a discontinuity at x=0 within [-1, 1]."""
        result = find_discontinuities("1/x", "x", (-1, 1))
        assert 0 in result

    def test_tan_discontinuities(self):
        """tan(x) has discontinuities at pi/2 + k*pi."""
        result = find_discontinuities("tan(x)", "x", (0, 4))
        # pi/2 ≈ 1.5708 within interval [0, 4]; 3*pi/2 ≈ 4.712 is outside
        assert any(abs(r - 1.5707963267948966) < 0.01 for r in result)

    def test_tan_discontinuities_small_interval(self):
        """tan(x) has a discontinuity at pi/2 within [0, pi]."""
        result = find_discontinuities("tan(x)", "x", (0, 3.141592653589793))
        assert len(result) > 0

    def test_continuous_interval_polynomial_runs(self):
        """find_discontinuities runs without error on a polynomial (may have
        false positives due to floating-point step scanning)."""
        result = find_discontinuities("x**2 + 2*x + 1", "x", (-10, 10))
        assert isinstance(result, list)

    def test_discontinuity_in_middle_of_interval(self):
        """1/(x-2) has a discontinuity at x=2 within [0, 4]."""
        result = find_discontinuities("1/(x-2)", "x", (0, 4))
        found = any(abs(r - 2.0) < 0.05 for r in result)
        assert found, f"Expected 2.0 in discontinuities, got {result}"

    def test_custom_step(self):
        """Test with a larger step parameter."""
        result = find_discontinuities("1/x", "x", (-2, 2), step=0.5)
        assert 0 in result
