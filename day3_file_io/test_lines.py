
import pytest
from lines import count_lines, check_arguments


def test_counts_code_only():
    code = [
        "# a comment\n",
        "\n",
        "import sys\n",
        "    # indented comment\n",
        "def main():\n",
        "    print('# not a comment')\n",   # code that CONTAINS # still counts
        "   \n",
    ]
    assert count_lines(code) == 3


def test_empty():
    assert count_lines([]) == 0


def test_real_file():
    with open("sample_code.py") as file:
        assert count_lines(file) == 3


def test_bad_arguments():
    # sys.exit() raises SystemExit, so we can test for it like any exception
    with pytest.raises(SystemExit):
        check_arguments(["lines.py"])
    with pytest.raises(SystemExit):
        check_arguments(["lines.py", "a.py", "b.py"])
    with pytest.raises(SystemExit):
        check_arguments(["lines.py", "notes.txt"])


def test_good_argument():
    assert check_arguments(["lines.py", "hello.py"]) == "hello.py"
