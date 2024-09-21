from seasons import day
import pytest

def test_main():
    assert day('2024-07-17')=="One thousand, four hundred forty minutes"
    assert day('2022-07-08') == "One million, sixty-seven thousand forty minutes"

def test_main_false():
    with pytest.raises(SystemExit, match="Invalid"):
            day('2024-20-20')
