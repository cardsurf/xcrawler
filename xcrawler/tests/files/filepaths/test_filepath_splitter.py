import unittest

import mock

from xcrawler.files.filepaths.filepath_splitter import FilePathSplitter


class TestFilePathSplitter(unittest.TestCase):

    def setUp(self):
        self.filepath_splitter = FilePathSplitter()

    @mock.patch('xcrawler.files.filepaths.filepath_splitter.os.path.splitext')
    def test_get_file_extension(self, mock_splitext_function):
        mock_file_path = "mock/path/to/file.txt"
        mock_splitext_function.return_value = ["file", ".txt"]
        result = self.filepath_splitter.get_file_extension(mock_file_path)
        self.assertEquals(result, ".txt")
