

import validate
import validate_no_regex


def test_regex_good_emails():
    assert validate.is_valid("malan@harvard.edu") == True
    assert validate.is_valid("b.ndayisenga@sfu.edu") == True


def test_regex_bad_emails():
    assert validate.is_valid("malan@harvard.com") == False    # wrong ending
    assert validate.is_valid("malanharvard.edu") == False     # no @
    assert validate.is_valid("malan@@harvard.edu") == False   # two @
    assert validate.is_valid("@harvard.edu") == False         # no username
    assert validate.is_valid("malan@harvard.edu.org") == False  # $ stops this
    assert validate.is_valid("ma lan@harvard.edu") == False   # space
    assert validate.is_valid("malan@harvard_edu") == False    # \. needs a real dot


def test_no_regex_version_basic():
    assert validate_no_regex.is_valid("malan@harvard.edu") == True
    assert validate_no_regex.is_valid("malan@harvard.com") == False


def test_no_regex_version_is_fooled():
    # These are NOT real emails, but the no-regex version accepts them.
    # This test documents the weakness the lecture talks about.
    assert validate_no_regex.is_valid("ma lan@harvard.edu") == True
    assert validate_no_regex.is_valid("malan@.edu") == True
