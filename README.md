"""
# Overly Sarcastic Calculator

A simple Python calculator with a sarcastic twist. Supports basic arithmetic operations: addition, subtraction, multiplication, and division. Includes unit tests using pytest.

---

## Features

- Addition, subtraction, multiplication, and division
- Humorous, sarcastic feedback for each operation
- Handles edge cases like division by zero (returns None)
- Unit tests to ensure correctness of operations

---

## Installation

1. Clone the repository:

    git clone <your-repo-url>
    cd <repo-directory>

2. (Optional) Create a virtual environment:

    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies (pytest):

    pip install pytest

---

## Usage

Run the calculator:

    python calculator.py

You’ll see a sarcastic greeting and be prompted to choose an operation:

    aaaaaaahhhh
    what do you want?
    Hurry up and Pick what calculations you want to do?
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    Enter the number of your choice (1-4):

Follow the prompts to enter numbers. The calculator will perform the operation and respond sarcastically.

---

## Testing

The project includes unit tests for all operations.

Run tests using:

    pytest test_calculator.py

Tests cover:

- Addition of positive and negative numbers
- Subtraction of large and negative numbers
- Multiplication including zero
- Division including division by zero and decimal results

---

## Notes

- Division by zero returns None to avoid crashing the program.
- Modify calculator.py to handle more advanced operations if desired.
"""
