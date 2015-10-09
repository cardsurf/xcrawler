
from xcrawler.compatibility.compatibility_factory import CompatibilityFactory
from xcrawler.files.writers.object_writer_csv import ObjectWriterCsv


class WriterFactory:

    def __init__(self):
        pass

    def create_object_writer_csv(self):
        factory = CompatibilityFactory()
        file_opener = factory.create_compatible_write_opener()
        object_converter = factory.create_compatible_object_converter()
        object_writer_csv = ObjectWriterCsv(file_opener, object_converter)
        return object_writer_csv

