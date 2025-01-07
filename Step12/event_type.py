from enum import Enum
from Src.Core.validator import validator

"""
Типы событий
"""
class event_type(Enum):
    DELETE_NOMENCLATURE = 1
    CHANGE_NOMENCLATURE = 2
    CHANGE_RANGE = 3
    CHANGE_BLOCK_PERIOD = 4
    SAVE_DATA = 5
    LOAD_DATA = 6