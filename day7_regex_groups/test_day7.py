
from email_better import is_valid
from format_name import format_name
from twitter import username_sub, username_search


def test_email_good():
    assert is_valid("malan@harvard.edu") == True
    assert is_valid("malan@cs50.harvard.edu") == True     # optional subdomain
    assert is_valid("b.ndayisenga@sfu.ca") == True        # dot in username
    assert is_valid("MALAN@HARVARD.EDU") == True          # IGNORECASE flag


def test_email_bad():
    assert is_valid("malan@harvard.net") == False
    assert is_valid("malan@harvard") == False
    assert is_valid("mal an@harvard.edu") == False


def test_format_name():
    assert format_name("Malan, David") == "David Malan"
    assert format_name("Malan,David") == "David Malan"        # no space
    assert format_name("Malan,   David") == "David Malan"     # many spaces
    assert format_name("David Malan") == "David Malan"        # no comma: unchanged


def test_username_sub():
    assert username_sub("https://twitter.com/davidjmalan") == "davidjmalan"
    assert username_sub("http://www.twitter.com/davidjmalan") == "davidjmalan"
    assert username_sub("twitter.com/davidjmalan") == "davidjmalan"


def test_username_search():
    assert username_search("https://www.twitter.com/davidjmalan") == "davidjmalan"
    assert username_search("https://google.com/davidjmalan") == None   # not twitter
