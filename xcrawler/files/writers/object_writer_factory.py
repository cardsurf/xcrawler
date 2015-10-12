
from xcrawler.compatibility.compatibility_factory import CompatibilityFactory
from xcrawler.files.writers.object_writer_csv import ObjectWriterCsv


class ObjectWriterFactory(object):

    def __init__(self,
                 compatibility_factory=CompatibilityFactory()):
        self.compatibility_factory = compatibility_factory

    def create_object_writer_csv(self):
        file_opener = self.compatibility_factory.create_compatible_write_opener()
        object_converter = self.compatibility_factory.create_compatible_object_converter()
        object_writer_csv = ObjectWriterCsv(file_opener, object_converter)
        return object_writer_csv

