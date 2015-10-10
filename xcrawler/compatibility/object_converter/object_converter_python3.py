
from xcrawler.compatibility.object_converter.compatible_object_converter import CompatibleObjectConverter


class ObjectConverterPython3(CompatibleObjectConverter):
    """A Python 3 compatible class for converting objects to strings.

    """
    def convert_to_string(self, o):
        if not self.instance_resolver.is_byte_string(o):
            o = str(o)
        return o

    def list_convert_to_string(self, list_objects):
        list_strings = self.list_convert_to_unicode_string(list_objects)
        return list_strings

