

class FileWriteOpener:
    """A class with methods for opening a file in a write mode.

    """

    def open_file_write_byte_strings(self, file_name):
        opened_file = open(file_name, "wb")
        return opened_file

    def open_file_write_unicode_strings(self, file_name):
        opened_file = open(file_name, "w", encoding='utf-8')
        return opened_file
