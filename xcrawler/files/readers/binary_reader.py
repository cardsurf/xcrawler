

from xcrawler.files.openers.read_opener import ReadOpener


class BinaryReader(object):
    """Reads a file content as byte strings"

    """
    def __init__(self,
                 file_opener=ReadOpener()):
        self.file_opener = file_opener
        self.file_name = ""
        self.file = None

    def open(self, file_name):
        self.file_name = file_name
        self.file = self.file_opener.open_file_read_byte_strings(file_name)

    def read_bytes(self, bytes_to_read):
        content = self.file.read(bytes_to_read)
        return content

    def close(self):
        self.file.close()
