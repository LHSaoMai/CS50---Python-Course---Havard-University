from um import count

def test_count():
    assert count('um')==1
    assert count('um?')==1

def test_count_word():
    assert count('Um, thanks for the album.')==1


def test_count_ponctuation():
    assert count('Um, thanks, um...')==2
