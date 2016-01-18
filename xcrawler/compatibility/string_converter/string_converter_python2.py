
from xcrawler.compatibility.string_converter.compatible_string_converter import CompatibleStringConverter


class StringConverterPython2(CompatibleStringConverter):
    """A Python 2 compatible class for converting a string to a specified type.

    """
    def convert_to_string(self, string):
        string = self.try_convert_to_byte_string_utf8(string)
        return string

    def list_convert_to_string(self, list_strings):
        return [self.try_convert_to_byte_string_utf8(s) for s in list_strings]

