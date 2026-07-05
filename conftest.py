import pytest

@pytest.fixture()
def user_data():
    return {
        "name": "Bray",
        "job": "Software Engineer"
    }


def pytest_html_report_title(report):
    report.title = "API pytest requests report"