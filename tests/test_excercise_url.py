import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from session_manager import make_session
from exercise_url import exercise_url
from test_app import app
import pytest
from tests.test_app import mock_app

@pytest.fixture(scope='session')
def test_session():
    session = make_session()
    return session


def test_url_validations(test_session):
    assert exercise_url(test_session,'Á://127.0.0.1:5000') == False
    assert exercise_url(test_session,'http://127.0.0.1:5000') != False
