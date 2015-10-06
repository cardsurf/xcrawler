
from xcrawler.compatibility.file_write_opener.compatible_file_write_opener import CompatibleFileWriteOpener


class FileWriteOpenerPython3(CompatibleFileWriteOpener):
    """A Python 3 compatible class for opening a file in a write mode.

    """
    def open_file_write_strings(self, file_name):
        opened_file = self.open_file_write_unicode_strings(file_name)
        return opened_file

