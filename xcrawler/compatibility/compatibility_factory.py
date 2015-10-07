
from xcrawler.utils.info.python_info import PythonInfo
from xcrawler.compatibility.write_opener.write_opener_python2 import WriteOpenerPython2
from xcrawler.compatibility.write_opener.write_opener_python3 import WriteOpenerPython3
from xcrawler.compatibility.object_converter.object_converter_python2 import ObjectConverterPython2
from xcrawler.compatibility.object_converter.object_converter_python3 import ObjectConverterPython3


class CompatibilityFactory:

    def __init__(self, python_info=PythonInfo()):
        self.python_info = python_info

    def create_compatible_write_opener(self):
        if self.python_info.is_python2():
            return WriteOpenerPython2()
        else:
            return WriteOpenerPython3()

    def create_compatible_object_converter(self):
        if self.python_info.is_python2():
            return ObjectConverterPython2()
        else:
            return ObjectConverterPython3()