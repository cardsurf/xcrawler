
import abc


class ObjectWriter:
    """A base class for writing objects to a file in a specified format.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def open_file(self, file_name):
        """
        Opens a file in a write mode.
        :param file_name: the name of a file to be opened in a write mode.
        """

    @abc.abstractmethod
    def write_headers(self, instance_object):
        """
        Writes headers to a file.
        :param instance_object: the first object to be written to a file.
        """

    @abc.abstractmethod
    def write_object(self, instance_object):
        """
        Writes an object to a file.
        If an object is not a string then a string representation of the object is used.
        :param instance_object: the object to be written to a file.
        """


