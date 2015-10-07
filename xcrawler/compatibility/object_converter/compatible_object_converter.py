
import abc

from xcrawler.utils.converters.object_converter import ObjectConverter


class CompatibleObjectConverter(ObjectConverter):
    """A Python 2 and 3 compatible class for converting objects to string.

    """
    @abc.abstractmethod
    def list_convert_to_string(self, list_objects):
        pass

