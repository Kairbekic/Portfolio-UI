# Portfolio UI Automation Framework

UI automation framework for end-to-end testing of a web application using Selenium, Pytest, Docker and Allure Reports.


## 🔗 Repository

GitHub: https://github.com/Kairbekic/Portfolio-UI


## Project Overview

This project demonstrates a scalable UI automation framework built for web application testing.
The framework follows the **Page Object Model (POM)** design pattern and includes reporting, containerization and CI/CD integration.

The project covers key QA automation practices used in real teams:
- UI test automation
- Test architecture using Page Object Model
- Fixtures and reusable components
- Dockerized test execution
- Allure reporting
- CI/CD integration with GitHub Actions
---


## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming language |
| Pytest | Test framework |
| Selenium WebDriver | UI automation |
| Allure Report | Test reporting |
| Docker | Containerized execution |
| GitHub Actions | CI/CD |
| Page Object Model | Test architecture |
---



## Project Structure

```text
portfolio-ui/
│
├── pages/ # Page Object classes
├── base/ # Base classes
├── tests/ # Test cases
├── config/ # Test configuration and data
├── utils/ # Helper methods
├── conftest.py # Pytest fixtures
├── requirements.txt # Project dependencies
├── pytest.ini # Pytest configuration
├── docker-compose.yml # Docker configuration
└── .github/workflows/ # GitHub Actions CI
```


## Features

✅ UI automation using Selenium
✅ Page Object Model (POM) architecture
✅ Reusable Pytest fixtures
✅ Explicit waits and loader synchronization
✅ Allure reporting with screenshots
✅ Dockerized test execution
✅ CI/CD with GitHub Actions
✅ End-to-end UI test scenario for employee management module


## Automated Test Scenario

Implemented end-to-end employee management flow:
1. Login to application
2. Navigate to employee section
3. Create employee
4. Verify employee creation
5. Delete employee
6. Verify employee deletion


## Installation

Clone repository:
```bash
    git clone https://github.com/Kairbekic/Portfolio-UI.git
    cd Portfolio-UI
```

Create virtual environment:
```bash
    python -m venv .venv
```

Activate environment (Windows):
```bash
    .venv\Scripts\activate
```

Install dependencies:
```bash
    pip install -r requirements.txt
```


## Run Tests

Run all tests:
```bash
    pytest -s -v
```

Run specific test:
```bash
    pytest tests/create_employee_test.py -s -v
```


## Allure Report

Generate results:
```bash
    pytest --alluredir=allure-results
```

Open report:
```bash
    allure serve allure-results
```


## Run with Docker
```bash
  docker-compose up --exit-code-from regression
```





## CI/CD

The project uses GitHub Actions for:
- automated test execution
- Docker-based test running
- Allure report generation
- 

## Author

**Madiyar Kairbekov**
GitHub: https://github.com/Kairbekic