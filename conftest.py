import os
import uuid

import pytest
import json
from datetime import datetime
from datetime import date
from utils.database_helper import insert
from pytest_jsonreport.plugin import JSONReport

# que alcance quiero que los fixtures tengan?
# https://betterprogramming.pub/understand-5-scopes-of-pytest-fixtures-1b607b5c19ed

pytest_plugins = [
    'fixtures.driver',
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
    print('\n***** Session Finished *****')
    report = session.config._json_report.report
    results = report['tests']
    data = []
    for result in results:
        insert(report['execution_id'], report['execution_date'], result['nodeid'], result['outcome'])
        # data.append({
        #     'execution_id': report['execution_id'],
        #     'execution_date': str(report['execution_date']),
        #     'test_name': result['nodeid'],
        #     'outcome': result['outcome']
        # })
    # print(report)

    now = datetime.now()  # current date and time
    date_time = now.strftime("results_%Y_%m_%d_%H:%M:%S")
    path = os.getcwd() + os.sep + 'results' + os.sep + date_time + '.json'
    with open(path, 'w') as f:
        json.dump(results, f, ensure_ascii=False)
    


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



def pytest_json_modifyreport(json_report):
    # Add a key to the report
    today = date.today()
    json_report['execution_date'] = today
    json_report['execution_id'] = str(uuid.uuid4())
    del json_report['duration']
    del json_report['exitcode']
    del json_report['environment']
    del json_report['collectors']
