from twttr import shorten

def test_shorten_lowercase():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_shorten_highcase():
    assert shorten("HALLO")=="HLL"

def test_shorten_nothing():
    assert shorten("CS50") == "CS50"
