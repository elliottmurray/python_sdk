import os
from enum import Enum


class CI(Enum):
    NONE = 0
    CIRCLECI = 1
    TRAVIS = 2
    JENKINS = 3
    TEAMCITY = 4

def detect_ci():
    if(os.getenv('CIRCLECI') == 'true'):
        return CI.CIRCLECI
    if(os.getenv('TRAVIS') == 'true'):
        return CI.TRAVIS
    if(os.getenv('JENKINS_URL') is not None):
        return CI.JENKINS
    if(os.getenv('TEAMCITY_VERSION') is not None):
        return CI.TEAMCITY

    return CI.NONE
