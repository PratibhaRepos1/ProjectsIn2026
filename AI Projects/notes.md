**Day 1 — Complete Python Development Setup & Basic Syntax**

- **Purpose:** : Quick, hands-on Day 1 checklist to set up a Python development environment and learn core syntax essentials.

**Prerequisites**
- **OS:**: Windows (these commands work on macOS/Linux with small adjustments).
- **Admin rights:**: Helpful for installing system packages.

**Setup: Install Python & Tools**
- **Check Python:**: Run `python --version` or `python3 --version` to confirm installation.
- **Install Python:**: Download from https://www.python.org/downloads/ and install (add to PATH).
- **Upgrade pip:**: `python -m pip install --upgrade pip`.
- **Create virtual env:**: `python -m venv venv` then activate with `venv\\Scripts\\activate` on Windows.
- **Install editor:**: Install Visual Studio Code and open the project with `code .`.
- **Recommended VS Code extensions:**: Python, Pylance, and Code Runner.

**Quick Project Init**
- **Project folder:**: Create a folder for your project and open it in VS Code.
- **requirements file:**: If you have dependencies, create `requirements.txt` and run `pip install -r requirements.txt`.

**Basic Python Syntax (Quick Reference)**
- **Variables:**: `x = 10`, `name = "Alice"`
- **Types:**: `int`, `float`, `str`, `list`, `tuple`, `dict`, `bool`.
- **Print:**: `print("Hello, world")`
- **Lists:**: create `nums = [1, 2, 3]`, append `nums.append(4)`.
- **Tuples:**: `coords = (10, 20)` (immutable).
- **Dictionaries:**: `person = {"name": "Deesha", "age": 34}`; access `person['name']`.
- **Conditionals:**:
	- `if x > 5:`
			- `print('x is big')`
- **Loops:**:
	- `for n in nums:`
			- `print(n)`
	- `while condition:`

**Functions**
- **Define:** `def greet(name):` then `return f"Hello {name}"`.

**File: Running & Testing**
- **Run script:**: `python first.py` (from this project folder).
- **Check syntax quickly:**: `python -m py_compile first.py`.

**Helpful Tips**
- **Keep virtual env active** when working (`venv\\Scripts\\activate`).
- **Use `requirements.txt`** to pin dependencies: `pip freeze > requirements.txt`.
- **Use linting/type checks**: enable Pylance in VS Code and run `flake8` or `pylint` if desired.

**Day 1 Example Snapshot**
- **Example file:** copy the provided `first.py` into the project root and run `python first.py` to see basic prints and data types in action.

**Next steps**
- **Day 2 suggestion:**: Learn functions, modules, and file I/O. Start a small script that reads/writes a text file.

---
_Edited: Day 1 setup and basic syntax guide_

