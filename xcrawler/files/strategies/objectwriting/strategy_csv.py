
import abc
import csv

from .strategy_object_writing import StrategyObjectWriting


class StrategyCsv(StrategyObjectWriting):
    """A base strategy of writing objects to a .csv file."

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, output_file):
        super(StrategyCsv, self).__init__(output_file)
        self.writer = csv.writer(output_file, delimiter=' ', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')


