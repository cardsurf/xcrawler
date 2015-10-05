
from xcrawler.pythonutils import string_utils
from xcrawler.files.strategies.objectwriting.strategy_csv import StrategyCsv


class StrategyCsvPython2(StrategyCsv):
    """A strategy of writing objects to a .csv file in Python 2"

    """
    def __init__(self, output_file):
        super(StrategyCsvPython2, self).__init__(output_file)

    def write(self, list_objects):
        list_objects = string_utils.list_convert_to_byte_string_utf8(list_objects)
        self.writer.writerow(list_objects)

