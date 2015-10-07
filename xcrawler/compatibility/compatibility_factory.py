
from xcrawler.utils.version_utils import is_python2
from xcrawler.compatibility.file_write_opener.file_write_opener_python2 import FileWriteOpenerPython2
from xcrawler.compatibility.file_write_opener.file_write_opener_python3 import FileWriteOpenerPython3
from xcrawler.compatibility.object_converter.object_converter_python2 import ObjectConverterPython2
from xcrawler.compatibility.object_converter.object_converter_python3 import ObjectConverterPython3


class CompatibilityFactory:

    def create_compatible_file_opener_write(self):
        if is_python2():
            return FileWriteOpenerPython2()
        else:
            return FileWriteOpenerPython3()

    def create_compatible_object_converter(self):
        if is_python2():
            return ObjectConverterPython2()
        else:
            return ObjectConverterPython3()