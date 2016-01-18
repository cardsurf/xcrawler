
from xcrawler.compatibility.string_converter.compatible_string_converter import CompatibleStringConverter


class StringConverterPython3(CompatibleStringConverter):
    """A Python 3 compatible class for converting a string to a specified type.

    """
    def convert_to_string(self, string):
        string = self.try_convert_to_unicode_string(string)
        return string

    def list_convert_to_string(self, list_strings):
        return [self.try_convert_to_unicode_string(s) for s in list_strings]

