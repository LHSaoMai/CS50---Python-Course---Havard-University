from numb3rs import validate

def test_numb3rs_number():
    assert validate('255.255.255.255')==True
    assert validate('256.255.255.255')==False

def test_numb3rs_letter():
     assert validate('cat')==False


def test_numb3rs_format():
     assert validate('255.255.255.255.255')==False

def test_numb3rs_first():
     assert validate('75.456.76.65')==False
