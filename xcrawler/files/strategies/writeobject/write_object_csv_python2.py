
from xcrawler.pythonutils import string_utils
from xcrawler.files.strategies.writeobject.write_object_csv import WriteObjectCsv


class WriteObjectCsvPython2(WriteObjectCsv):
    """A strategy of writing objects to a .csv file in Python 2"

    """
    def __init__(self, output_file):
        super(WriteObjectCsvPython2, self).__init__(output_file)

    def write(self, list_objects):
        list_objects = string_utils.list_convert_to_byte_string_utf8(list_objects)
        self.writer.writerow(list_objects)

