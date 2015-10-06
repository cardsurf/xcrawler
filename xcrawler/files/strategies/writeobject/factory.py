
from xcrawler.pythonutils.version_utils import is_python2
from xcrawler.files.strategies.writeobject.write_object_csv_python2 import WriteObjectWriterCsvPython2
from xcrawler.files.strategies.writeobject.write_object_csv_python3 import WriteObjectWriterCsvPython3


def create_csv_strategy(output_file):
    if is_python2():
        return WriteObjectWriterCsvPython2(output_file)
    else:
        return WriteObjectWriterCsvPython3(output_file)

