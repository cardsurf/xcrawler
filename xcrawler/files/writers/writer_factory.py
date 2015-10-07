
from xcrawler.compatibility.compatibility_factory import CompatibilityFactory
from xcrawler.files.writers.item_writer import ItemWriter
from xcrawler.files.writers.object_writer_csv import ObjectWriterCsv


class WriterFactory:

    def create_item_writer_based_on_file_extension(self, file_name):
        extension = file_name.split(".")[-1]
        if extension == "csv":
            return self.create_item_writer_csv()

        raise ValueError("Not supported file extension: " + extension)

    def create_item_writer_csv(self):
        object_writer = self.create_object_writer_csv()
        item_writer = ItemWriter(object_writer)
        return item_writer

    def create_object_writer_csv(self):
        factory = CompatibilityFactory()
        file_opener = factory.create_compatible_file_opener_write()
        object_to_string_converter = factory.create_compatible_object_string_converter()
        object_writer_csv = ObjectWriterCsv(file_opener, object_to_string_converter)
        return object_writer_csv

