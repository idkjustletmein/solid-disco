"""
Unit tests for calculate.py age calculator
"""
import pytest
import sys
import os
from io import StringIO

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculate import judge_leap_year, month_days


def test_judge_leap_year_true():
    """Test leap year detection for actual leap years"""
    assert judge_leap_year(2020) == True
    assert judge_leap_year(2024) == True
    assert judge_leap_year(2000) == True


def test_judge_leap_year_false():
    """Test leap year detection for non-leap years"""
    assert judge_leap_year(2021) == False
    assert judge_leap_year(2022) == False
    assert judge_leap_year(2023) == False
    assert judge_leap_year(1900) == False  # Not divisible by 400


def test_month_days_31():
    """Test months with 31 days"""
    assert month_days(1, False) == 31   # January
    assert month_days(3, False) == 31   # March
    assert month_days(5, False) == 31   # May
    assert month_days(7, False) == 31   # July
    assert month_days(8, False) == 31   # August
    assert month_days(10, False) == 31  # October
    assert month_days(12, False) == 31  # December


def test_month_days_30():
    """Test months with 30 days"""
    assert month_days(4, False) == 30   # April
    assert month_days(6, False) == 30   # June
    assert month_days(9, False) == 30   # September
    assert month_days(11, False) == 30  # November


def test_month_days_february_leap():
    """Test February in leap year"""
    assert month_days(2, True) == 29


def test_month_days_february_non_leap():
    """Test February in non-leap year"""
    assert month_days(2, False) == 28


def test_leap_year_edge_cases():
    """Test edge cases for leap years"""
    assert judge_leap_year(2000) == True   # Divisible by 400
    assert judge_leap_year(1900) == False  # Divisible by 100 but not 400
    assert judge_leap_year(2100) == False  # Divisible by 100 but not 400
    assert judge_leap_year(2400) == True   # Divisible by 400
