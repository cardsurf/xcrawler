
import unittest
import mock

from xcrawler.compatibility.compatibility_factory import CompatibilityFactory
from xcrawler.compatibility.write_opener.compatible_write_opener import CompatibleWriteOpener
from xcrawler.compatibility.object_converter.compatible_object_converter import CompatibleObjectConverter
from xcrawler.files.writers.object_writer import ObjectWriter
from xcrawler.files.writers.object_writer_factory import ObjectWriterFactory


class TestObjectWriterFactory(unittest.TestCase):

    def setUp(self):
        compatibility_factory = mock.create_autospec(CompatibilityFactory).return_value
        self.object_writer_factory = ObjectWriterFactory(compatibility_factory)

    @mock.patch('xcrawler.files.writers.object_writer_factory.ObjectWriterCsv')
    def test_create_object_writer_csv(self, mock_object_writer_csv_class):
        mock_write_opener = mock.create_autospec(CompatibleWriteOpener).return_value
        mock_object_converter = mock.create_autospec(CompatibleObjectConverter).return_value
        mock_object_writer = mock.create_autospec(ObjectWriter).return_value
        self.object_writer_factory.compatibility_factory.create_compatible_write_opener.return_value = mock_write_opener
        self.object_writer_factory.compatibility_factory.create_compatible_object_converter.return_value = mock_object_converter
        mock_object_writer_csv_class.return_value = mock_object_writer
        result = self.object_writer_factory.create_object_writer_csv()
        mock_object_writer_csv_class.assert_called_once_with(mock_write_opener, mock_object_converter)
        self.assertEquals(result, mock_object_writer)




