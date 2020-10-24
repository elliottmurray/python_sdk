import os

from mock import patch
import pytest

from open_analytics.ci_matcher import detect_ci, CI


def mockenv(**envvars):
    return patch.dict(os.environ, envvars)

@mockenv(CIRCLECI='')
def test_local_ci():
    assert detect_ci() == CI.NONE


@mockenv(CIRCLECI='true')
# @patch.dict(os.environ, {"CIRCLECI": "true"})
def test_circle_ci():
    assert detect_ci() == CI.CIRCLECI


# @patch.dict(os.environ, {"TRAVIS": "true"})
@mockenv(TRAVIS='true')
@mockenv(CIRCLECI='')
def test_travis_ci():
    assert detect_ci() == CI.TRAVIS


# @patch.dict(os.environ, {"JENKINS_URL": "some value"})
@mockenv(JENKINS_URL='some value')
@mockenv(CIRCLECI='')
def test_jenkins_ci():
    assert detect_ci() == CI.JENKINS
