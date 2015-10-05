
from xcrawler.pythonutils import version_utils


class FileOpenerWrite:
    """A class with methods for opening a file in a write mode.

    """

    def open_file_write_strings(self, output_file_name):
        if version_utils.is_python2():
            return self.open_file_write_byte_strings(output_file_name)
        else:
            return self.open_file_write_unicode_strings(output_file_name)

    def open_file_write_byte_strings(self, output_file_name):
        output_file = open(output_file_name, "wb")
        return output_file

    def open_file_write_unicode_strings(self, output_file_name):
        output_file = open(output_file_name, "w", encoding='utf-8')
        return output_file
