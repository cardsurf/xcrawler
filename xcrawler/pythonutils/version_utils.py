
from sys import version_info


def is_python2():
    return version_info.major == 2


def is_python3():
    return version_info.major == 3



