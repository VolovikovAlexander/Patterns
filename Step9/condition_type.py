from enum import Enum

"""
Варианты сравнения
"""
class condition_type(Enum):
    """
    Равно
    """
    EQUALS = 1
    """
    Примерно
    """
    LIKE = 2
    """
    Меньше или равно
    """
    LESSOREQUALS = 3

    """
    Сформировать словарь с вариантами формата
    """
    @staticmethod
    def list():
        result = {}
        for item in condition_type:
            result[item.name] = item.value   

        return result     