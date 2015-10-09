
import unittest
import mock
import csv

from xcrawler.files.writers.csv_writer import CsvWriterFactory


class TestCsvWriterFactory(unittest.TestCase):

    def setUp(self):
        self.csv_writer_factory = CsvWriterFactory()

    @mock.patch('xcrawler.files.writers.csv_writer.csv.writer')
    def test_csv_writer(self, mock_csv_writer_class):
        mock_opened_file = mock.Mock()
        mock_csv_writer = mock.create_autospec(csv.writer).return_value
        mock_csv_writer_class.return_value = mock_csv_writer
        result = self.csv_writer_factory.create_csv_writer(mock_opened_file)
        self.assertEquals(result, mock_csv_writer)
