
from xcrawler.pythonutils import string_utils
from xcrawler.files.strategies.writeobject.write_object_csv import WriteObjectCsv


class WriteObjectCsvPython3(WriteObjectCsv):
    """A strategy of writing objects to a .csv file in Python 3"

    """
    def __init__(self, output_file):
        super(WriteObjectCsvPython3, self).__init__(output_file)

    def write(self, list_objects):
        list_objects = string_utils.list_convert_to_unicode_strings(list_objects)
        self.writer.writerow(list_objects)

