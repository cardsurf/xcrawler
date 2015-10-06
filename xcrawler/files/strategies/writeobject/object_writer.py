
import abc


class ObjectWriter:
    """A base class for strategy of writing objects to a file in a specific format.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def open_file(self, file_name):
        """
        Opens a file in a write mode.
        :param file_name: the name of a file to be opened in a write mode.
        """

    @abc.abstractmethod
    def write_headers(self, item):
        """
        Writes headers to a file.
        :param item: the first item to be written to a file.
        """

    @abc.abstractmethod
    def write_item(self, item):
        """
        Writes an item to a file.
        If an item is not a string then a string representation of the item is used.
        :param item: the item to be written to a file.
        """


