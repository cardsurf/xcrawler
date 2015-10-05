
from ....pythonutils.version_utils import is_python2
from .strategy_write_byte_strings import StrategyWriteByteStrings
from .strategy_write_unicode_strings import StrategyWriteUnicodeStrings


def create_strings_strategy():
    if is_python2():
        return StrategyWriteByteStrings()
    else:
        return StrategyWriteUnicodeStrings()
