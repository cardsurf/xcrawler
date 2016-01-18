
import abc

from xcrawler.pythonutils.converters.string_converter import StringConverter


class CompatibleStringConverter(StringConverter):
    """A Python 2 and 3 compatible class for converting a string to a specified type.

    """
    @abc.abstractmethod
    def convert_to_string(self, instance_object):
        pass

    @abc.abstractmethod
    def list_convert_to_string(self, list_objects):
        pass

