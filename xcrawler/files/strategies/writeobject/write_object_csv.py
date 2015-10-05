
import abc
import csv

from xcrawler.files.strategies.writeobject.write_object_strategy import WriteObjectStrategy


class WriteObjectCsv(WriteObjectStrategy):
    """A base strategy of writing objects to a .csv file."

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, output_file):
        super(WriteObjectCsv, self).__init__(output_file)
        self.writer = csv.writer(output_file, delimiter=' ', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')


