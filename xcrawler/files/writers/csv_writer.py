
import csv

class CsvWriterFactory(object):
    """Creates an instance of the csv.writer class.

    """
    def __init__(self):
        pass

    def create_csv_writer(self, opened_file, delimiter=' ', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n'):
        csv_writer = csv.writer(opened_file,
                                delimiter=delimiter,
                                quotechar=quotechar,
                                quoting=quoting,
                                lineterminator=lineterminator)
        return csv_writer
