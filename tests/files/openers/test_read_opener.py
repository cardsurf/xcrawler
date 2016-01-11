
import unittest
import mock
try:
    import __builtin__ as builtins
except ImportError:
    import builtins

from xcrawler.files.openers.read_opener import ReadOpener


class TestReadOpener(unittest.TestCase):

    def setUp(self):
        self.read_opener = ReadOpener()

    @mock.patch('tests.files.openers.test_read_opener.builtins.open')
    def test_open_file_read_byte_strings(self, mock_open_function):
        mock_file_name = "file.csv"
        mock_file = mock.Mock()
        mock_open_function.return_value = mock_file
        result = self.read_opener.open_file_read_byte_strings(mock_file_name)
        self.assertEquals(result, mock_file)
