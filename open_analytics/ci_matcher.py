import os
from enum import Enum 


class CI(Enum):
    NONE = 0
    CIRCLECI = 1
    TRAVIS = 2
    JENKINS = 3

# CI_ENVS = [
# 'CI',
# 'CONTINUOUS_INTEGRATION',
# 'ABSTRUSE_BUILD_DIR',
# 'APPVEYOR',
# 'BUDDY_WORKSPACE_URL',
# 'BUILDKITE',
# 'CF_BUILD_URL',
# 'CIRCLECI',
# 'CODEBUILD_BUILD_ARN',
# 'CONCOURSE_URL',
# 'DRONE',
# 'GITLAB_CI',
# 'GO_SERVER_URL',
# 'JENKINS_URL',
# 'PROBO_ENVIRONMENT',
# 'SEMAPHORE',
# 'SHIPPABLE',
# 'TDDIUM',
# 'TEAMCITY_VERSION',
# 'TF_BUILD',
# 'TRAVIS',
# 'WERCKER_ROOT',
# ];


def detect_ci():
    print("!!!")
    print(os.environ)
    print(os.getenv('CIRCLECI'))
    if(os.getenv('CIRCLECI') == 'true'):
        return CI.CIRCLECI
    if(os.getenv('TRAVIS') == 'true'):
        return CI.TRAVIS
    if(os.getenv('JENKINS_URL') is not None):
        return CI.JENKINS

    return CI.NONE
