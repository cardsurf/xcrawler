
from xcrawler.compatibility.object_converter.compatible_object_converter import CompatibleObjectConverter


class ObjectConverterPython2(CompatibleObjectConverter):
    """A Python 2 compatible class for converting objects to strings.

    """
    def convert_to_string(self, o):
        if not self.instance_resolver.is_unicode_string(o):
            o = str(o)
        return o

    def list_convert_to_string(self, list_objects):
        list_strings = self.list_convert_to_byte_string_utf8(list_objects)
        return list_strings

