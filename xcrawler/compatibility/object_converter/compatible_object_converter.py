
import abc

from xcrawler.pythonutils.converters.object_converter import ObjectConverter


class CompatibleObjectConverter(ObjectConverter):
    """A Python 2 and 3 compatible class for converting an object to a specified type.

    """
    @abc.abstractmethod
    def convert_to_string(self, instance_object):
        pass

    @abc.abstractmethod
    def list_convert_to_string(self, list_objects):
        pass

