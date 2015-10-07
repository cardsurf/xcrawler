
from xcrawler.compatibility.compatibility_factory import CompatibilityFactory
from xcrawler.files.writers.item_writer import ItemWriter
from xcrawler.files.writers.object_writer_csv import ObjectWriterCsv
from xcrawler.utils.filepaths.filepath_splitter import FilePathSplitter


class WriterFactory:

    def __init__(self, filepath_splitter=FilePathSplitter()):
        self.filepath_splitter = filepath_splitter

    def create_item_writer_based_on_file_extension(self, file_name):
        extension = self.filepath_splitter.get_file_extension(file_name)
        if extension == ".csv":
            return self.create_item_writer_csv()

        raise ValueError("Not supported file extension: " + extension)

    def create_item_writer_csv(self):
        object_writer = self.create_object_writer_csv()
        item_writer = ItemWriter(object_writer)
        return item_writer

    def create_object_writer_csv(self):
        factory = CompatibilityFactory()
        file_opener = factory.create_compatible_write_opener()
        object_converter = factory.create_compatible_object_converter()
        object_writer_csv = ObjectWriterCsv(file_opener, object_converter)
        return object_writer_csv

