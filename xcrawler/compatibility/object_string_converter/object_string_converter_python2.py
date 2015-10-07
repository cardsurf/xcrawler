
from xcrawler.utils import string_utils
from xcrawler.compatibility.object_string_converter.compatible_object_string_converter import CompatibleObjectStringConverter


class ObjectStringConverterPython2(CompatibleObjectStringConverter):
    """A Python 2 compatible class for converting objects to strings.

    """
    def list_convert_to_string(self, list_objects):
        list_strings = string_utils.list_convert_to_byte_string_utf8(list_objects)
        return list_strings

