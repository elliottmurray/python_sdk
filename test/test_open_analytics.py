import requests
import os

from open_analytics.open_analytics import install_start_event
from open_analytics.open_analytics import detect_ci

from mock import patch

@patch.dict(os.environ, {"CIRCLECI": "true"})
@patch('requests.post')
def test_send_message(mock_post):
    install_start_event(2, 'pytest')

    mock_post.assert_called_once()


@patch('open_analytics.open_analytics.detect_ci')
@patch('requests.post')
def test_check_ci(mock_post, mock_detect_ci):
    install_start_event(2, 'pytest')

    mock_post.assert_called_once()
    mock_detect_ci.assert_called_once()



