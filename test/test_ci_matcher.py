import os

from mock import patch
import pytest

from open_analytics.ci_matcher import detect_ci, CI


@pytest.fixture
def unset_circleci():
    patch('os.environ', {'CIRCLECI', None})


def test_local_ci(unset_circleci):
    assert detect_ci() == CI.NONE


@patch.dict(os.environ, {"CIRCLECI": "true"})
def test_circle_ci():
    assert detect_ci() == CI.CIRCLECI


@patch.dict(os.environ, {"TRAVIS": "true"})
def test_travis_ci(unset_circleci):
    assert detect_ci() == CI.TRAVIS


@patch.dict(os.environ, {"JENKINS_URL": "some value"})
def test_jenkins_ci(unset_circleci):
    assert detect_ci() == CI.JENKINS
