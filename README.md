*This project has been created as part of the 42 curriculum by thdeglos.*

# Growing Code — Python Module 00

## Description

**Growing Code** is an introductory Python project from the 42 curriculum. It teaches the fundamental syntax and semantics of Python (expressions, variables, functions, control flow and type hints) through small scenarios inspired by community garden data: harvest totals, plant age, watering reminders, seed inventory, and so on.

Each exercise is a single function that handles its own input and output. There is no main program: the functions are meant to be imported and tested with the `main.py` helper provided with the subject.

### Exercises

| Ex | Directory | File | Concept practiced |
|----|-----------|------|-------------------|
| 0 | `ex0/` | `ft_hello_garden.py` | Defining a function, `print()` |
| 1 | `ex1/` | `ft_garden_name.py` | `input()`, f-strings |
| 2 | `ex2/` | `ft_plot_area.py` | `int()`, arithmetic expressions |
| 3 | `ex3/` | `ft_harvest_total.py` | Variables, sums |
| 4 | `ex4/` | `ft_plant_age.py` | Conditions (`if` / `else`), strict comparison (`> 60`) |
| 5 | `ex5/` | `ft_water_reminder.py` | Conditions (`> 2` days) |
| 6 | `ex6/` | `ft_count_harvest_iterative.py`<br>`ft_count_harvest_recursive.py` | `for` + `range()`, recursion with a nested helper |
| 7 | `ex7/` | `ft_seed_inventory.py` | Type hints, string methods (`capitalize`), `if` / `elif` / `else` |

## Instructions

### Requirements

- Python 3.10 or later
- `flake8` (code style) and `mypy` (type checking, required for exercise 7)

### Project structure

```
Python_Module00/
├── ex0/ft_hello_garden.py
├── ex1/ft_garden_name.py
├── ex2/ft_plot_area.py
├── ex3/ft_harvest_total.py
├── ex4/ft_plant_age.py
├── ex5/ft_water_reminder.py
├── ex6/ft_count_harvest_iterative.py
├── ex6/ft_count_harvest_recursive.py
└── ex7/ft_seed_inventory.py
```

### Running the functions

The files contain only function definitions, so they do nothing when run directly. The subject provides a `main.py` helper to test them. It is **not** part of the submission and is not committed in this repository.

Copy `main.py` into the directory of the exercise you want to test (it imports the exercise files from its own folder), then run it and pick an exercise:

```bash
cp /path/to/main.py ex2/
cd ex2
python3 main.py
```

```
🌱 Welcome to Growing Code! 🌱
...
Enter your choice: 2

=== Testing ft_plot_area ===
Enter length: 5
Enter width: 3
Plot area: 15
```

Choice `6` runs both the iterative and the recursive version of exercise 6, and `7` runs exercise 7 with several seed types and units, including an unknown one.

Alternatively, import and call a function directly, from inside an exercise directory:

```bash
cd ex2
python3 -c "from ft_plot_area import ft_plot_area; ft_plot_area()"
```

```
Enter length: 5
Enter width: 3
Plot area: 15
```

Exercise 7 takes arguments:

```bash
cd ex7
python3 -c "from ft_seed_inventory import ft_seed_inventory; ft_seed_inventory('tomato', 15, 'packets')"
```

```
Tomato seeds: 15 packets available
```

Supported units for exercise 7: `packets`, `grams`, `area`. Any other unit prints `Unknown unit type`.

### Checks

```bash
flake8 ex*/
mypy ex7/ft_seed_inventory.py
```

## Resources

- [Python documentation](https://docs.python.org/3/)
- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [PEP 484 — Type Hints](https://peps.python.org/pep-0484/)
- [flake8 documentation](https://flake8.pycqa.org/)
- [mypy documentation](https://mypy.readthedocs.io/)

### Use of AI

AI (Claude, by Anthropic) was used to help redacting this README.
