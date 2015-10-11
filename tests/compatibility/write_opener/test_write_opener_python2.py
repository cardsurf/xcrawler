
import unittest
import mock

from xcrawler.compatibility.write_opener.write_opener_python2 import WriteOpenerPython2


class TestWriteOpenerPython2(unittest.TestCase):

    def setUp(self):
        self.write_opener = WriteOpenerPython2()

    @mock.patch.object(WriteOpenerPython2, 'open_file_write_byte_strings')
    def test_open_file_write_strings(self, mock_open_file_write_byte_strings):
        mock_filename = "file.csv"
        mock_file = mock.Mock()
        mock_open_file_write_byte_strings.return_value = mock_file
        result = self.write_opener.open_file_write_strings(mock_filename)
        self.assertEquals(result, mock_file)
