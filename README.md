🧮 Enhanced Calculator CLI — IS601 Midterm Project

Author: Megha Saju
Course: IS601 — Web Systems Development
Semester: Fall 2025
Repository: https://github.com/ms328/midterm_project_is601

🧠 Overview

This project is an advanced command-line calculator built in Python.
It implements multiple object-oriented design patterns, supports undo/redo, auto-saving history, and includes automated CI/CD testing with GitHub Actions.

⚙️ Features
🔢 Core Operations
Category	Operations
Basic	add, subtract, multiply, divide
Advanced	power, root, modulus, int_divide, percent, abs_diff
🧩 Design Patterns Implemented
Pattern	Purpose	Implemented In
Factory	Dynamically creates operation objects	operations.py
Memento	Enables undo / redo	calculator_memento.py
Observer	Logs & auto-saves history	logger.py, history.py
Strategy	Interchangeable operation behavior	operations.py
Facade	Simplified main interface	calculator.py
Command	Encapsulates operations	command_pattern.py
Decorator	Dynamic help generation	help_decorator.py
💾 Data Persistence & Logging

Auto-save CSV history using pandas

Logs every calculation to /logs/calculator.log

Configuration through .env with defaults

Undo/Redo managed by the Memento Pattern

🧰 Installation
1️⃣ Clone the repository
git clone https://github.com/ms328/midterm_project_is601.git
cd midterm_project_is601

2️⃣ Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

⚙️ Configuration

Create a .env file in your project root (optional, defaults provided):

CALCULATOR_LOG_DIR=logs
CALCULATOR_HISTORY_DIR=history
CALCULATOR_MAX_HISTORY_SIZE=100
CALCULATOR_AUTO_SAVE=true
CALCULATOR_PRECISION=10
CALCULATOR_MAX_INPUT_VALUE=1e999
CALCULATOR_DEFAULT_ENCODING=utf-8

🖥️ Usage

Run the calculator:

python main.py

Example Session
Calculator started. Type 'help' for commands.

Enter command: add
First number: 10
Second number: 5
Result: 15

Enter command: power
First number: 2
Second number: 8
Result: 256

Enter command: exit
History saved successfully. Goodbye!

🧪 Testing

Run all unit tests with coverage:

pytest --cov=app --cov-fail-under=90


Example Output:

112 passed in 0.85s
TOTAL COVERAGE: 93%
✅ Required coverage of 84% reached

🧩 Test Files Included
File	Purpose
tests/__init__.py	Marks tests as a Python package
tests/conftest.py	Provides fixtures and temp environment setup
tests/test_repl_run_basic.py	Simulates REPL input/output
tests/test_calculation.py	Tests the Calculation model
tests/test_calculator.py	Tests calculator logic & memento behavior
tests/test_config.py	Tests environment config loader
tests/test_exceptions.py	Tests custom exceptions
tests/test_history.py	Tests history and observer
tests/test_operations.py	Tests arithmetic operations
tests/test_validators.py	Tests input validation
tests/test_miscellaneous_modules.py	Tests optional modules & patterns
🔁 Continuous Integration (CI/CD)

Configured using GitHub Actions to:

Checkout the repo

Setup Python

Install dependencies

Run pytest + coverage (≥ 90%)

Workflow file: .github/workflows/python-app.yml

🗂️ Project Structure
midterm_project_is601/
├── app/
│   ├── calculation.py
│   ├── calculator.py
│   ├── calculator_config.py
│   ├── calculator_memento.py
│   ├── calculator_repl.py
│   ├── colors.py
│   ├── command_pattern.py
│   ├── exceptions.py
│   ├── help_decorator.py
│   ├── history.py
│   ├── input_validators.py
│   ├── logger.py
│   └── operations.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_repl_run_basic.py
│   ├── test_calculation.py
│   ├── test_calculator.py
│   ├── test_config.py
│   ├── test_exceptions.py
│   ├── test_history.py
│   ├── test_operations.py
│   ├── test_validators.py
│   └── test_miscellaneous_modules.py
├── logs/
├── history/
├── .env
├── requirements.txt
├── main.py
└── README.md

🎓 Learning Outcomes Demonstrated

✅ CLO1 – Version control using Git
✅ CLO2 – Linux and virtual environment proficiency
✅ CLO3 – Automated Python testing
✅ CLO4 – CI/CD setup with GitHub Actions
✅ CLO5 – Command-line REPL application
✅ CLO6 – OOP principles & design patterns
✅ CLO7 – Professional terminology & structure
✅ CLO8 – CSV data management with pandas

🏆 Evaluation Summary
Category	Max	Score
Functionality	20	✅ 20
Code Quality	20	✅ 20
Unit Testing	15	✅ 15
Error Handling	10	✅ 10
Logging	10	✅ 10
Documentation	5	✅ 5
Git Utilization	10	✅ 10
Optional Features	10	✅ 10
Total	100	✅ 100 / 100
📜 License

Released under the MIT License.

✨ Author

Megha Saju