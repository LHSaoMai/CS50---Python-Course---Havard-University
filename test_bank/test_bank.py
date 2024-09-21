from bank import value

def test_value_hello():
    assert value('hello')== 0
    assert value('HeLLo')== 0

def test_value_h():
    assert value('holeofm')== 20
    assert value('Hi')== 20

def test_value_other():
    assert value('kijif')== 100
    assert value('W!!?j')== 100
