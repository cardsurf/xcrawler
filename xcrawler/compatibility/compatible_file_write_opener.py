
import abc

from xcrawler.files.openers.file_write_opener import FileWriteOpener


class CompatibleFileWriteOpener(FileWriteOpener):
    """A Python 2 and 3 compatible class for opening a file in a write mode.

    """
    @abc.abstractmethod
    def open_file_write_strings(self, file_name):
        pass




