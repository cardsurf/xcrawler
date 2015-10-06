
from xcrawler.pythonutils import version_utils
from xcrawler.files.openers.file_opener_write import FileOpenerWrite


class CompatibleFileOpenerWrite:
    """A Python 2 and 3 compatible class for opening a file in a write mode.

    """
    def __init__(self):
        self.open_file_write_strings = self.get_open_file_write_strings()

    def get_open_file_write_strings(self):
        if version_utils.is_python2():
            return FileOpenerWrite.open_file_write_byte_strings
        else:
            return FileOpenerWrite.open_file_write_unicode_strings

