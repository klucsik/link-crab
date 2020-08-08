import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from session_manager import make_session
from url_gatherer import get_all_website_links
from test_app import app
import pytest
from tests.test_excercise_url import test_session
from tests.test_app import mock_app

def test_url_gathering(test_session):
    links = set()
    assert len(get_all_website_links(test_session,'http://127.0.0.1:5000', links)) == 8
