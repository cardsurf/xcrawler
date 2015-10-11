
import unittest
import mock

from xcrawler.compatibility.write_opener.write_opener_python3 import WriteOpenerPython3


class TestWriteOpenerPython3(unittest.TestCase):

    def setUp(self):
        self.write_opener = WriteOpenerPython3()

    @mock.patch.object(WriteOpenerPython3, 'open_file_write_unicode_strings')
    def test_open_file_write_strings(self, mock_open_file_write_unicode_strings):
        mock_filename = "file.csv"
        mock_file = mock.Mock()
        mock_open_file_write_unicode_strings.return_value = mock_file
        result = self.write_opener.open_file_write_strings(mock_filename)
        self.assertEquals(result, mock_file)
