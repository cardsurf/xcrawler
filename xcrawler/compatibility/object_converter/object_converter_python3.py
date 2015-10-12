
from xcrawler.compatibility.object_converter.compatible_object_converter import CompatibleObjectConverter


class ObjectConverterPython3(CompatibleObjectConverter):
    """A Python 3 compatible class for converting an object to a specified type.

    """
    def convert_to_string(self, instance_object):
        if not self.instance_resolver.is_byte_string(instance_object):
            instance_object = str(instance_object)
        return instance_object

    def list_convert_to_string(self, list_objects):
        list_strings = self.list_convert_to_unicode_string(list_objects)
        return list_strings

