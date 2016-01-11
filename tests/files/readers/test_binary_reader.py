
import unittest
import mock


from xcrawler.files.readers.binary_reader import BinaryReader
from xcrawler.files.openers.read_opener import ReadOpener


class TestBinaryReader(unittest.TestCase):

    def setUp(self):
        mock_read_opener = mock.create_autospec(ReadOpener).return_value
        self.binary_reader = BinaryReader(mock_read_opener)
        self.binary_reader.file = mock.Mock()
        self.binary_reader.file_name = "mock.txt"

    def test_open(self):
        mock_file_name = "mock.txt"
        mock_file = mock.Mock()
        self.binary_reader.file_opener.open_file_read_byte_strings.return_value = mock_file
        self.binary_reader.open(mock_file_name)
        self.assertEquals(self.binary_reader.file, mock_file)

    def test_read_bytes(self):
        mock_bytes_to_read = 11
        mock_content = "First chars"
        self.binary_reader.file.read.return_value = mock_content
        result = self.binary_reader.read_bytes(mock_bytes_to_read)
        self.assertEquals(result, mock_content)

    def test_close(self):
        self.binary_reader.close()
        self.binary_reader.file.close.assert_called_once_with()