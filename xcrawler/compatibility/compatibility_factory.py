
from xcrawler.pythonutils.version_utils import is_python2
from xcrawler.compatibility.file_write_opener_python2 import FileWriteOpenerPython2
from xcrawler.compatibility.file_write_opener_python3 import FileWriteOpenerPython3
from xcrawler.compatibility.object_string_converter_python2 import ObjectStringConverterPython2
from xcrawler.compatibility.object_string_converter_python3 import ObjectStringConverterPython3


class CompatibilityFactory:

    def create_compatible_file_opener_write(self):
        if is_python2():
            return FileWriteOpenerPython2()
        else:
            return FileWriteOpenerPython3()

    def create_compatible_object_string_converter(self):
        if is_python2():
            return ObjectStringConverterPython2()
        else:
            return ObjectStringConverterPython3()