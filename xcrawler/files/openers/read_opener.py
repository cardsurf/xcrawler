
class ReadOpener(object):
    """Opens a file in a read mode.

    """
    def __init__(self):
        pass

    def open_file_read_byte_strings(self, file_name):
        opened_file = open(file_name, "rb")
        return opened_file

