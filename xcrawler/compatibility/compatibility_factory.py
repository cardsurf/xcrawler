
from xcrawler.pythonutils.version_utils import is_python2
from xcrawler.compatibility.file_opener_write_python2 import FileOpenerWritePython2
from xcrawler.compatibility.file_opener_write_python3 import FileOpenerWritePython3
from xcrawler.compatibility.object_string_converter_python2 import ObjectStringConverterPython2
from xcrawler.compatibility.object_string_converter_python3 import ObjectStringConverterPython3


class CompatibilityFactory:

    def create_compatible_file_opener_write(self):
        if is_python2():
            return FileOpenerWritePython2()
        else:
            return FileOpenerWritePython3()

    def create_compatible_object_string_converter(self):
        if is_python2():
            return ObjectStringConverterPython2()
        else:
            return ObjectStringConverterPython3()