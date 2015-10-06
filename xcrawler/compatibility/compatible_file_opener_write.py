
import abc

from xcrawler.files.openers.file_opener_write import FileOpenerWrite


class CompatibleFileOpenerWrite(FileOpenerWrite):
    """A Python 2 and 3 compatible class for opening a file in a write mode.

    """
    @abc.abstractmethod
    def open_file_write_strings(self, file_name):
        pass




