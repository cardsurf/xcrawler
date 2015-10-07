
from xcrawler.utils import string_utils
from xcrawler.compatibility.object_converter.compatible_object_converter import CompatibleObjectConverter


class ObjectConverterPython3(CompatibleObjectConverter):
    """A Python 3 compatible class for converting objects to strings.

    """
    def list_convert_to_string(self, list_objects):
        list_strings = string_utils.list_convert_to_unicode_string(list_objects)
        return list_strings

