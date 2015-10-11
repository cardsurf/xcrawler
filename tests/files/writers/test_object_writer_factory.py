
import unittest
import mock

from xcrawler.compatibility.compatibility_factory import CompatibilityFactory
from xcrawler.files.writers.object_writer_factory import ObjectWriterFactory


class TestObjectWriterFactory(unittest.TestCase):

    def setUp(self):
        self.factory = ObjectWriterFactory()

    @mock.patch('xcrawler.files.writers.object_writer_factory.CompatibilityFactory')
    @mock.patch('xcrawler.files.writers.object_writer_factory.ObjectWriterCsv')
    def test_create_object_writer_csv(self, mock_object_writer_csv_class, mock_compatibility_factory_class):
        mock_factory_instance = mock.create_autospec(CompatibilityFactory).return_value
        mock_file_opener = mock.Mock()
        mock_object_converter = mock.Mock()
        mock_object_writer = mock.Mock()

        mock_compatibility_factory_class.return_value = mock_factory_instance
        mock_factory_instance.create_compatible_write_opener.return_value = mock_file_opener
        mock_factory_instance.create_compatible_object_converter.return_value = mock_object_converter
        mock_object_writer_csv_class.return_value = mock_object_writer
        result = self.factory.create_object_writer_csv()
        mock_object_writer_csv_class.assert_called_once_with(mock_file_opener, mock_object_converter)
        self.assertEquals(result, mock_object_writer)




