# PyQt Calculator

A GUI based calculator that can do maths from basic level, up to advanced level.


---

## Table of Contents
- [About](#about)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running](#running)
- [Testing](#testing)
- [Development / PyCharm notes](#development--pycharm-notes)
- [Code style & linters](#code-style--linters)
- [Git / Workflow](#git--workflow)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## About
PyQt Calculator is a personal project created to test problem-solving skills while also serving as a practical tool for a student’s daily needs.  
The goal is to combine a clean, user-friendly PyQt interface with the ability to handle both simple arithmetic and advanced mathematical operations.

---

## Features
- **Basic calculator functions**: addition, subtraction, multiplication, division  
- **Scientific functions**: sin, cos, tan, log, ln, exp, sqrt, factorial  
- **Memory functions**: M+, M−, MR, MC  
- **History panel**: view past calculations using QListWidget or QTextEdit  
- **Equation solver**: powered by SymPy for solving algebraic equations  
- **Graphing tab**: plot functions with matplotlib embedded in a QWidget  
- **Themes**: switch between dark and light modes using Qt stylesheets  
- **Error handling**: e.g., displays “Math Error” for invalid operations such as division by zero


---

## Requirements
- Python 3.10+  
- [PyQt5](https://pypi.org/project/PyQt5/) (GUI framework)  
- [SymPy](https://www.sympy.org/) (symbolic mathematics)  
- [Matplotlib](https://matplotlib.org/) (graphing and visualization)  
- [NumPy](https://numpy.org/) (scientific computing support)  
- Other supporting libraries: contourpy, cycler, fonttools, kiwisolver, pillow, pyparsing, python-dateutil, six  

### Recommended tools
- [PyCharm](https://www.jetbrains.com/pycharm/) (Community or Professional Edition) for development and debugging  

## Installation

### Clone the repository
```bash
git clone https://github.com/<your-username>/pyqt-calculator.git
cd pyqt-calculator
```
### Install dependencies
```
pip install -r requirements.txt
```
### Running

To launch the calculator, run the following command from the project root:
```
python main.py
```
Alternatively, open the project in PyCharm and run main.py directly from the IDE.

## Testing
Testing support will be added in future updates.  
For now, no automated test suite is available. You can manually verify features by running `main.py` and trying different calculator operations.

## Development / PyCharm notes
- Open the project folder in **PyCharm** (Community or Professional).  
- Create and select a **Python virtual environment** when prompted, or configure one manually under *Settings → Project → Python Interpreter*.  
- Install the dependencies inside PyCharm’s terminal with:
```bash
  pip install -r requirements.txt
```
- Run the project by right-clicking main.py and selecting Run 'main'.

- Use PyCharm’s built-in debugger to step through the code and inspect variables.

- Optional: configure a run/debug configuration for main.py so you can launch the calculator with a single click.

## Code style & linters
This project follows the [PEP 8](https://peps.python.org/pep-0008/) style guide for Python code.  
While no specific linter is enforced, tools such as **flake8** or **pylint** can be used to check for style issues, and **black** may be used for automatic formatting.

## Git / Workflow
This project uses Git and GitHub for version control.

A typical workflow looks like this:
1. **Clone the repository**  
```bash
   git clone https://github.com/<your-username>/pyqt-calculator.git
```
Create a new branch for your feature or bugfix

bash
Copy code
git checkout -b feature-name

Commit your changes with clear messages

```bash
git add .
git commit -m "Describe your changes"
```
Push your branch to GitHub

```bash
git push origin feature-name
```
Open a Pull Request on GitHub to merge your branch into main.

## Contributing
This is primarily a personal project, but suggestions and improvements are welcome.  
If you’d like to contribute, please fork the repository and open a pull request on GitHub.

## License
No license has been specified for this project yet.

## Contact
For questions or suggestions, please reach out via GitHub:  
[https://github.com/weebdev123](https://github.com/<your-username>)
