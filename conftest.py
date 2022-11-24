import os

import pytest

# que alcance quiero que los fixtures tengan?
# https://betterprogramming.pub/understand-5-scopes-of-pytest-fixtures-1b607b5c19ed

pytest_plugins = [
    'fixtures.driver'
]

"""
@pytest.fixture(name="test")
def test_hook():
    print('**** Test Started ****')

    yield
    print('\n**** Test Ended ****')

"""


def pytest_configure(config):
    """
    Allows plugins and conftest files to perform initial configuration.
    This hook is called for every plugin and initial conftest
    file after command line options have been parsed.
    """
    print('***** Execution Started *****')

    if os.environ.get("EXECUTION_ID") is None:
        execution_id = config.getoption('--env')
    else:
        execution_id = os.environ.get("EXECUTION_ID")

    print(f'execution_id = {execution_id}')


def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """
    print('***** Session Start *****')


def pytest_sessionfinish(session, exitstatus):
    """
    Called after whole test run finished, right before
    returning the exit status to the system.
    """
    print('***** Session Finished *****')


def pytest_unconfigure(config):
    """
    called before test process is exited.
    """
    print('***** Execution Ended *****')


def pytest_addoption(parser):
    """
    Adding options to the CLI for execution variables

    Args:
        parser (pytest.config.argparsing.Parser): [description]
    """
    parser.addoption('--env', action='store', help="Execution environment")
