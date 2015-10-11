
from sys import version_info


class PythonInfo(object):
    """Gets information about the version of Python.

    """
    def __init__(self):
        pass

    def is_python2(self):
        return version_info.major == 2

    def is_python3(self):
        return version_info.major == 3

