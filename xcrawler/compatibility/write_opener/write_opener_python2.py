
from xcrawler.compatibility.write_opener.compatible_write_opener import CompatibleWriteOpener


class WriteOpenerPython2(CompatibleWriteOpener):
    """A Python 2 compatible class for opening a file in a write mode.

    """
    def open_file_write_strings(self, file_name):
        opened_file = self.open_file_write_byte_strings(file_name)
        return opened_file
