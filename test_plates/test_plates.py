from plates import is_valid

def test_start_letters():
    assert is_valid('CS50')==True
    assert is_valid('CS05')==False
    assert is_valid('CS50P')==False

def test_character():
    assert is_valid('CS50456')==False
    assert is_valid('D')==False

def test_notzero():
    assert is_valid('CS50P')==False


def test_middle():
    assert is_valid('PI3.14')==False

def test_space_period():
    assert is_valid('ER_TF')==False


def test_OUTIME():
    assert is_valid('OUTATIME')==False

def test_beginning():
    assert is_valid('OU50')==True
    assert is_valid('5750')==False
