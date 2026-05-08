# AdNabu QA Assignment

This repository contains the submission for the AdNabu Quality Assurance Engineer assignment.

---

# Task 1 - Manual Test Design

Manual test cases for:
- Product Search
- Add to Cart

Location:
```text
test_cases/TEST_CASES.md
```

---

# Task 2 - Selenium Automation

Automated Scenario:
- Search product
- Add product to cart successfully
- Validate product added to cart

---

# Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Pytest HTML Report

---

# Project Structure

```text
automation/
├── tests/
├── utils/
├── config.py

reports/
└── report.html

test_cases/
└── TEST_CASES.md
```

---

# Setup Instructions

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Run Automation Test

```bash
pytest automation/tests/test_search_add_to_cart.py
```

---

# Generate HTML Report

```bash
pytest automation/tests/test_search_add_to_cart.py --html=reports/report.html --self-contained-html
```

---

# Test Report

Execution report available at:

```text
reports/report.html
reports/report.png
```