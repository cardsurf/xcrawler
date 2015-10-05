
import abc


class WriteObjectStrategy:
    """A base class for strategy of writing objects to a file in a specific format.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, output_file):
        self.output_file = output_file

    @abc.abstractmethod
    def write(self, list_objects):
        """
        Writes a list of objects to a file.
        If an object is not a string then a string representation of the object is used.
        :param list_strings: the list of objects to be written to an output file.
        """
