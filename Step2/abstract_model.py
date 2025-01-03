from abc import ABC, abstractmethod
from Src.Core.validator import validator
import uuid


"""
Абстрактный класс для наследования моделей данных
"""
class abstract_model(ABC):
    __unique_code:str

    def __init__(self) -> None:
        super().__init__()
        self.__unique_code = uuid.uuid4().hex

    """
    Уникальный код
    """
    @property
    def unique_code(self) -> str:
        return self.__unique_code
    
    @unique_code.setter
    def unique_code(self, value: str):
        validator.validate(value, str)
        self.__unique_code = value.strip()
    

    """
    Вариант сравнения (по коду)
    """
    @abstractmethod
    def set_compare_mode(self, other_object) -> bool:
        if other_object is  None: return False
        if not isinstance(other_object, abstract_model): return False

        return self.__unique_code == other_object.unique_code
    
    """
    Дополнительный метод для десериализации
    """
    @abstractmethod
    def deserialize(self, data:dict ):
        validator.validate(data, dict)

    """
    Перегрузка штатного варианта сравнения
    """
    def __eq__(self, value: object) -> bool:
        return self.set_compare_mode(value)

       
    """
    Вернуть строковое представление
    """
    def __str__(self) -> str:
        return self.unique_code
    

    

   

        

        
