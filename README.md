Selenium Automation Project

This project contains automated end-to-end tests for https://www.saucedemo.com using Python, Selenium, and Pytest.

Requirements:

- Python 3.10+
- Google Chrome
- pip

Installation:

1. Create and activate a virtual environment

   Windows:
   python -m venv venv
   venv\Scripts\activate

2. Install dependencies:
   pip install -r requirements.txt

Running tests:

- To run all tests:
  pytest

- To run tests with HTML report:
  pytest --html=report.html --self-contained-html

- To run specific test types (e.g. e2e, regression):
  pytest -m e2e
  pytest -m regression
