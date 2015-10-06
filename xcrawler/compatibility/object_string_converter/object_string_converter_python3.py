
from xcrawler.pythonutils import string_utils
from xcrawler.compatibility.object_string_converter.compatible_object_string_converter import CompatibleObjectStringConverter


class ObjectStringConverterPython3(CompatibleObjectStringConverter):
    """A Python 3 compatible class for converting objects to strings.

    """
    def list_convert_to_string(self, list_objects):
        list_strings = string_utils.list_convert_to_unicode_string(list_objects)
        return list_strings

