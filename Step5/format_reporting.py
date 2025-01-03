from enum import Enum
from Src.Core.validator import validator

"""
Форматы отчетов
"""
class format_reporting(Enum):
    CSV = 1
    XML = 2
    JSON = 3
    MARKDOWN = 99

    """
    Сформировать словарь с вариантами формата
    """
    @staticmethod
    def list():
        result = {}
        for item in format_reporting:
            result[item.name] = item.value


        return result
    
    """
    Проверить корректность формата
    """
    @staticmethod
    def check(format:int) -> bool:
        validator.validate(format, int)
        for item in format_reporting:
            if item.value == format:
                return True
            

        return False    


