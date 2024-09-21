from working import convert
import pytest

def test_convert_date():
    assert convert('9 AM to 5 PM') =='09:00 to 17:00'
    assert convert('10 AM to 8:50 PM')=='10:00 to 20:50'


def test_convert_inverse():
    assert convert('10:30 PM to 8 AM') =='22:30 to 08:00'

def test_convert_out_of_range():
    with pytest.raises(ValueError):
            convert('9 AM - 5 PM')


def test_convert_out():
    with pytest.raises(ValueError):
       convert('24 AM to 8 AM')
