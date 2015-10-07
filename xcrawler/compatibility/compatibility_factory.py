
from xcrawler.utils.version_utils import is_python2
from xcrawler.compatibility.write_opener.write_opener_python2 import WriteOpenerPython2
from xcrawler.compatibility.write_opener.write_opener_python3 import WriteOpenerPython3
from xcrawler.compatibility.object_converter.object_converter_python2 import ObjectConverterPython2
from xcrawler.compatibility.object_converter.object_converter_python3 import ObjectConverterPython3


class CompatibilityFactory:

    def create_compatible_write_opener(self):
        if is_python2():
            return WriteOpenerPython2()
        else:
            return WriteOpenerPython3()

    def create_compatible_object_converter(self):
        if is_python2():
            return ObjectConverterPython2()
        else:
            return ObjectConverterPython3()