
import abc


class StrategyFileOpening:
    """A base class for strategy of opening a file in a specific mode.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def open(self, file_name):
        """
        Opens a file with the name passed as the argument in a specific mode.
        :param file_name: the name of a file to open.
        :returns: an opened file.
        """