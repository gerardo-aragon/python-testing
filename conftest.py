import os
import uuid

import pytest
import json
from datetime import datetime
from datetime import date
import distutils
from  distutils import util
from utils.database_helper import insert
from pytest_jsonreport.plugin import JSONReport

pytest_plugins = [
    'fixtures.driver',
    'fixtures.auth'
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
    for result in results:
        # save test_name and feature_name
        test_name = result['nodeid'].split('::')[2]
        feature = result['nodeid'].split('::')[1][4:]
        #  convert outcome to boolean
        outcome = result['outcome']
        if outcome == "passed":
            outcome = True
        else:
            outcome = False
        # Save results on database
        insert(report['execution_id'], report['execution_date'], feature, test_name, outcome)

    path = os.getcwd() + os.sep + 'results' + os.sep + report['execution_date'] + '.json'
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
    parser.addoption('--password', action='store', default="Test123@", help="Password auth")


def pytest_json_modifyreport(json_report):
    """
    Modify json report
    :param json_report: json report to modify
    :return: modified json report
    """

    now = datetime.now()  # current date and time
    # Add a key to the report
    date_time = now.strftime("%Y_%m_%d_%H:%M:%S")
    json_report['execution_date'] = date_time
    json_report['execution_id'] = str(uuid.uuid4())
    # delete section on the report
    del json_report['created']
    del json_report['root']
    del json_report['duration']
    del json_report['exitcode']
    del json_report['environment']
    del json_report['collectors']
