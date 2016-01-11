
from xcrawler.files.openers.write_opener import WriteOpener
from xcrawler.files.readers.binary_reader import BinaryReader
import os


class BinaryWriter(object):
    """Writes byte strings to a file.

    """
    def __init__(self,
                 file_opener=WriteOpener(),
                 binary_reader=BinaryReader()):
        self.file_opener = file_opener
        self.binary_reader = binary_reader
        self.file_name = ""
        self.file = None

    def open(self, file_name):
        self.file_name = file_name
        self.file = self.file_opener.open_file_write_byte_strings(file_name)

    def replace(self, file_name, current_string, new_string):
        temp_file_name = "temp_" + file_name
        self.open(temp_file_name)
        self.replace_in_temp_file(file_name, current_string, new_string)
        self.close()
        self.rename_temp_file(temp_file_name, file_name)

    def replace_in_temp_file(self, file_name, current_string, new_string):
        self.binary_reader.open(file_name)
        self.replace_and_write(current_string, new_string)
        self.binary_reader.close()

    def replace_and_write(self, current_string, new_string):
        hundred_mbs = 100 * 1000000
        byte_string = self.binary_reader.read_bytes(hundred_mbs)
        while len(byte_string) > 0:
            byte_string = byte_string.replace(current_string, new_string)
            self.write(byte_string)
            byte_string = self.binary_reader.read_bytes(hundred_mbs)

    def rename_temp_file(self, temp_file_name, file_name):
        os.rename(temp_file_name, file_name)

    def write(self, byte_string):
        self.file.write(byte_string)

    def close(self):
        self.file.close()
