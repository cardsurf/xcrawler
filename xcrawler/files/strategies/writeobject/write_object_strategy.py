
import abc


class WriteObjectStrategy:
    """A base class for strategy of writing objects to a file in a specific format.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, output_file):
        self.output_file = output_file

    @abc.abstractmethod
    def write_headers(self, item):
        """
        Writes headers at the beginning of an output file.
        :param item: the first item to be written to an output file.
        """

    @abc.abstractmethod
    def write_item(self, item):
        """
        Writes an item to a file.
        If an item is not a string then a string representation of the item is used.
        :param item: the item to be written to an output file.
        """
