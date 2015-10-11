
import unittest
import mock

from xcrawler.pythonutils.info.python_info import PythonInfo


class TestPythonInfo(unittest.TestCase):

    def setUp(self):
        self.python_info = PythonInfo()

    @mock.patch('xcrawler.pythonutils.info.python_info.version_info')
    def test_is_python2(self, mock_version_info):
        mock_version_info.major = 2
        result = self.python_info.is_python2()
        self.assertEquals(result, True)

    @mock.patch('xcrawler.pythonutils.info.python_info.version_info')
    def test_is_python3(self, mock_version_info):
        mock_version_info.major = 3
        result = self.python_info.is_python3()
        self.assertEquals(result, True)
