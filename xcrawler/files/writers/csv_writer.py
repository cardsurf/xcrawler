
import csv

class CsvWriterFactory:
    """Creates an instance of the csv.writer class.

    """
    def __init__(self):
        pass

    def create_csv_writer(self, opened_file):
        csv_writer = csv.writer(opened_file)
        return csv_writer
