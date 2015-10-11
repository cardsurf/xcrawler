
import os


class FilePathSplitter(object):
    """Splits a path to a file into smaller parts.

    """
    def __init__(self):
        pass

    def get_file_extension(self, file_path):
        [file_name, file_extension] = os.path.splitext(file_path)
        return file_extension

