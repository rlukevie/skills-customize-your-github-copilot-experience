import pytest

from starter_code import apply_discount, calculate_total, student_grade


def test_calculate_total_adds_tax():
    assert calculate_total([10, 5], tax_rate=0.10) == 16.5


def test_calculate_total_empty_list():
    assert calculate_total([]) == 0.0


def test_apply_discount_20_percent():
    assert apply_discount(100, 20) == 80


def test_apply_discount_zero_percent():
    assert apply_discount(100, 0) == 100


@pytest.mark.parametrize(
    "score, expected",
    [
        (90, "A"),
        (80, "B"),
        (70, "C"),
        (60, "D"),
        (59, "F"),
    ],
)
def test_student_grade_boundaries(score, expected):
    assert student_grade(score) == expected
