
from .strategy_file_opening import StrategyFileOpening


class StrategyWriteUnicodeStrings(StrategyFileOpening):
    """A strategy of file opening that allows to write unicode strings to a file."

    """
    def __init__(self):
        super(StrategyFileOpening, self).__init__()

    def open(self, file_name):
        opened_file = open(file_name, "w", encoding='utf-8')
        return opened_file
