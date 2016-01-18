
from xcrawler.pythonutils.types.instance_resolver import InstanceResolver
from xcrawler.pythonutils.converters.string_converter import StringConverter


class ObjectConverter(object):
    """Converts an object to a specified type.

    """
    def __init__(self,
                 string_converter=StringConverter(),
                 instance_resolver=InstanceResolver()):
        self.string_converter = string_converter
        self.instance_resolver = instance_resolver

    def convert_to_byte_string_utf8(self, instance_object):
        string = self.convert_to_string(instance_object)
        byte_string_utf8 = self.string_converter.convert_to_byte_string_utf8(string)
        return byte_string_utf8

    def convert_to_unicode_string(self, instance_object):
        string = self.convert_to_string(instance_object)
        unicode_string = self.string_converter.convert_to_unicode_string(string)
        return unicode_string

    def convert_to_string(self, instance_object):
        if not self.instance_resolver.is_string_python_version(instance_object):
            instance_object = str(instance_object)
        return instance_object

    def convert_to_list_if_single_object(self, instance_object):
        if isinstance(instance_object, list):
            return instance_object
        return [instance_object]

    def list_convert_to_byte_string_utf8(self, list_objects):
        return [self.convert_to_byte_string_utf8(instance_object) for instance_object in list_objects]

    def list_convert_to_unicode_string(self, list_objects):
        return [self.convert_to_unicode_string(instance_object) for instance_object in list_objects]

    def list_convert_to_string(self, list_objects):
        return [self.convert_to_string(instance_object) for instance_object in list_objects]

