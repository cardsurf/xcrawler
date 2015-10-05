
from ....pythonutils.version_utils import is_python2
from .strategy_csv_python2 import StrategyCsvPython2
from .strategy_csv_python3 import StrategyCsvPython3


def create_csv_strategy(output_file):
    if is_python2():
        return StrategyCsvPython2(output_file)
    else:
        return StrategyCsvPython3(output_file)

