import pytest
from fuel import convert, gauge

def test_convert_int():
    with pytest.raises(ValueError):
        convert('1/cat')

def test_convert_zero():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_convert_number():
    assert convert('1/2')== 50
    assert convert('1/4')== 25

def test_gauge_zero():
    assert gauge(0.02)== 'E'
    assert gauge(50)== '50%'
    assert gauge(99)== 'F'

def test_gauge_one():
    assert gauge(1)== 'E'
