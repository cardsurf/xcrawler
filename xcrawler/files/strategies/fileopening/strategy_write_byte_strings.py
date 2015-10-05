
from .strategy_file_opening import StrategyFileOpening


class StrategyWriteByteStrings(StrategyFileOpening):
    """A strategy of file opening that allows to write byte strings to a file."

    """
    def __init__(self):
        super(StrategyFileOpening, self).__init__()

    def open(self, file_name):
        opened_file = open(file_name, "wb")
        return opened_file

