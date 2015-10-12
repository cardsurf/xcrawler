
from xcrawler.compatibility.object_converter.compatible_object_converter import CompatibleObjectConverter


class ObjectConverterPython2(CompatibleObjectConverter):
    """A Python 2 compatible class for converting an object to a specified type.

    """
    def convert_to_string(self, instance_object):
        if not self.instance_resolver.is_unicode_string(instance_object):
            instance_object = str(instance_object)
        return instance_object

    def list_convert_to_string(self, list_objects):
        list_strings = self.list_convert_to_byte_string_utf8(list_objects)
        return list_strings

