# Chitai-Gorod Selenium Test Automation

Automated UI testing framework for [Chitai-Gorod](https://www.chitai-gorod.ru) online bookstore using Selenium WebDriver and Pytest.

## Overview

This project implements automated tests for core functionality of the Chitai-Gorod website:
- Product search and shopping cart operations
- Site navigation and menu interactions
- Product catalog browsing
- Location/city switching

The framework uses Page Object Model (POM) design pattern for maintainable and scalable test architecture.

## Features

- Page Object Model architecture with separated page logic and test cases
- Parallel test execution via pytest-xdist
- HTML test reports
- Flexible test markers (smoke, regression, search, menu, catalog, location)
- Anti-detection measures for automation bypass
- Automatic screenshot capture on test failures
- Headless mode support for CI/CD pipelines

## Tech Stack

- Python 3.x
- Selenium WebDriver 4.38.0
- Pytest 8.4.2
- pytest-xdist 3.8.0 (parallel execution)
- pytest-html 3.2.0 (HTML reports)
- Chrome WebDriver

## Prerequisites

- Python 3.8+
- Google Chrome (latest version)
- Git

## Installation

Clone the repository:
```bash
git clone https://github.com/your-username/chitaigorod-selenium.git
cd chitaigorod-selenium
```

Create and activate virtual environment:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
chitaigorod-selenium/
├── config/
│   └── config.py                    # Base URL, browser settings, timeouts
├── pages/
│   ├── base_page.py                 # Base page class
│   ├── search_page.py               # Search and cart page
│   ├── menu_page.py                 # Navigation menu
│   ├── catalog_page.py              # Product catalog
│   └── change_location_page.py      # Location switcher
├── tests/
│   ├── test_search.py               # Search and cart tests
│   ├── test_menu.py                 # Menu navigation tests
│   ├── test_catalog.py              # Catalog tests
│   └── test_change_location.py      # Location tests
├── conftest.py                      # Pytest fixtures
├── pytest.ini                       # Pytest configuration
└── requirements.txt
```

## Running Tests

Run all tests:
```bash
pytest
```

Verbose output:
```bash
pytest -v
```

Run by markers:
```bash
pytest -m smoke           # Critical smoke tests
pytest -m search          # Search functionality
pytest -m menu            # Menu navigation
pytest -m catalog         # Catalog browsing
pytest -m location        # Location switching
```

Parallel execution (4 workers):
```bash
pytest -n 4
```

Generate HTML report:
```bash
pytest --html=reports/report.html --self-contained-html
```

Run specific test:
```bash
pytest tests/test_search.py::test_search_product
```

Combined commands:
```bash
# Smoke tests with report, 2 workers
pytest -m smoke -n 2 --html=reports/smoke_report.html --self-contained-html

# All tests with verbose output and report
pytest -v --html=reports/full_report.html --self-contained-html
```

## Configuration

### config/config.py

Core settings:
- `BASE_URL` - https://www.chitai-gorod.ru
- `BROWSER` - Chrome
- `IMPLICIT_WAIT` - 10 seconds
- `EXPLICIT_WAIT` - 15 seconds
- `PAGE_LOAD_TIMEOUT` - 30 seconds

### pytest.ini

Available markers:
- `smoke` - Critical tests for quick verification
- `regression` - Full regression test suite
- `search` - Product search tests
- `menu` - Navigation tests
- `catalog` - Catalog tests
- `location` - Location switching tests

## Test Cases

### test_search.py
- `test_search_product` - Search for book by author "Телевизор" and verify results
- `test_cart` - Add product to cart and remove from cart

### test_menu.py
- `test_certificate_menu` - Navigate to Certificates section
- `test_bonusProgram_menu` - Navigate to Bonus Program section
- `test_sale_menu` - Navigate to Sale section

### test_catalog.py
- `test_catalog_is_visible` - Verify catalog opens correctly
- `test_catalog_is_working` - Navigate through categories: Art Supplies > Paints > Gouache

### test_change_location.py
- `test_location_moscow` - Verify default location (Moscow)
- `test_change_location_to_kazan` - Change location to Kazan

**Total: 10 tests**

## Screenshots

Failed tests automatically capture screenshots to `screenshots/` directory with naming pattern:
```
screenshot_<test_name>_<timestamp>.png
```

## CI/CD

The framework supports headless mode for CI/CD environments. Headless mode activates automatically when `CI` environment variable is detected.

Example GitHub Actions configuration:
```yaml
- name: Run tests
  run: |
    pytest -m smoke --html=reports/report.html --self-contained-html
```

## Reports

HTML reports are generated in `reports/` directory when using `--html` flag. Open `report.html` in browser to view detailed test results.

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## Contact

For questions or suggestions, please open an issue in the repository.
