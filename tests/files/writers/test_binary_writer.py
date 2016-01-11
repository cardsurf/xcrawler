
import unittest
import mock

from xcrawler.files.writers.binary_writer import BinaryWriter
from xcrawler.files.openers.write_opener import WriteOpener
from xcrawler.files.readers.binary_reader import BinaryReader


class TestBinaryWriter(unittest.TestCase):

    def setUp(self):
        mock_file_opener = mock.create_autospec(WriteOpener).return_value
        mock_binary_reader = mock.create_autospec(BinaryReader).return_value
        self.binary_writer = BinaryWriter(mock_file_opener, mock_binary_reader)
        self.binary_writer.file = mock.Mock()
        self.binary_writer.file_name = "mock.txt"

    def test_open(self):
        mock_file_name = "mock.txt"
        mock_file = mock.Mock()
        self.binary_writer.file_opener.open_file_write_byte_strings.return_value = mock_file
        self.binary_writer.open(mock_file_name)
        self.assertEquals(self.binary_writer.file, mock_file)

    @mock.patch.object(BinaryWriter, 'replace_in_temp_file')
    @mock.patch.object(BinaryWriter, 'open')
    @mock.patch.object(BinaryWriter, 'close')
    @mock.patch.object(BinaryWriter, 'rename_temp_file')
    def test_replace(self, mock_rename_temp_file, mock_close, mock_open, mock_replace_in_temp_file):
        mock_file_name = "mock.txt"
        mock_current_string = b"line"
        mock_new_string = b"sentence"
        self.binary_writer.replace(mock_file_name, mock_current_string, mock_new_string)
        mock_replace_in_temp_file.assert_called_once_with(mock_file_name, mock_current_string, mock_new_string)

    @mock.patch.object(BinaryWriter, 'replace_and_write')
    def test_replace_in_temp_file(self, mock_replace_and_write):
        mock_file_name = "mock.txt"
        mock_current_string = b"line"
        mock_new_string = b"sentence"
        self.binary_writer.replace_in_temp_file(mock_file_name, mock_current_string, mock_new_string)
        mock_replace_and_write.assert_called_once_with(mock_current_string, mock_new_string)

    @mock.patch.object(BinaryWriter, 'write')
    def test_replace_and_write(self, mock_write):
        mock_current_content = b"This is the first line.\n This is the second line."
        mock_current_string = b"line"
        mock_new_string = b"sentence"
        mock_new_content = b"This is the first sentence.\n This is the second sentence."
        self.binary_writer.binary_reader.read_bytes.side_effect = [mock_current_content, ""]
        self.binary_writer.replace_and_write(mock_current_string, mock_new_string)
        mock_write.assert_called_once_with(mock_new_content)

    @mock.patch('xcrawler.files.writers.binary_writer.os.rename')
    def test_rename_temp_file(self, mock_rename):
        mock_file_name = "mock.txt"
        mock_temp_file_name = "temp_mock.txt"
        self.binary_writer.rename_temp_file(mock_temp_file_name,  mock_file_name )
        mock_rename.assert_called_once_with(mock_temp_file_name,  mock_file_name )

    def test_write(self):
        mock_byte_string = b"The first line to write.\n The second line to write."
        self.binary_writer.write(mock_byte_string)
        self.binary_writer.file.write.assert_called_once_with(mock_byte_string)

    def test_close(self):
        self.binary_writer.close()
        self.binary_writer.file.close.assert_called_once_with()

