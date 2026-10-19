# Unit Testing & File I/O in Python (CS50P Lectures 5–6)


Setup (once):
```
pip install pytest pillow
```


Friday run order:
```
python make_frames.py
python costumes.py frame1.gif frame2.gif frame3.gif frame4.gif
python los.py ../day4_csv/patients.csv summary.csv
python gif_maker.py frame1.gif frame2.gif frame3.gif frame4.gif
pytest -v
```

## What I learned each day
- **Mon:** `assert` raises `AssertionError` when a condition is false; pytest runs every `test_` function and reports each failure separately.
- **Tue:** Test by *category* (positive, negative, zero, boundaries, bad input). Use `pytest.raises` for errors. Functions should **return** values, not print, so they can be tested.
- **Wed:** `with open(...)` closes files automatically. `"w"` overwrites, `"a"` appends. `sorted()` with `reverse=True`.
- **Thu:** The `csv` library handles commas inside quoted values. `DictReader`/`DictWriter` use the header row. `key=lambda ...` controls what `sorted()` compares.
- **Fri:** PIL opens images and saves them as an animated GIF. Refactoring a script into functions makes file-processing code testable.



# – Regular Expressions & Object-Oriented Programming (CS50P Lectures 7–8)


Setup: nothing new to install (`re`, `csv`, `random` come with Python; pytest).


Friday run order:
```
python hat.py
python wizard.py
python vault.py
python duration.py
python triage_board.py admissions.txt board.csv
pytest -v
```

## What I learned each day
- **Mon:** A regex is a pattern. `^` and `$` anchor the start and end, `[ ]` lists allowed characters, `[^ ]` lists forbidden ones, `{m}` repeats exactly m times, and `\.` means a real dot.
- **Tue:** `\w` and `\d` are shortcuts; `( )` groups and captures; `re.IGNORECASE` ignores case; `fullmatch` checks the whole string; `:=` assigns inside an `if`; `re.sub` replaces matches.
- **Wed:** Tuples can't be changed, dicts can. A class is a blueprint, an object is one thing made from it, `__init__` sets its attributes, and methods use `self`.
- **Thu:** Raise `ValueError` for bad data. `__str__` controls `print()`. `@property` and setters validate every change, not just at creation.
- **Fri:** `@classmethod` works on the class itself. Child classes reuse the parent with `super().__init__()`. `__add__` defines what `+` does.



