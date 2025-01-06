from abc import ABC, abstractmethod


"""
Абстрактный класс прототип
"""
class abstract_prototype(ABC):
    __data = []

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def create(self):
        pass
    
    """
    Полученный набор данных
    """
    @property
    def data(self) -> list:
        return self.__data    
    
    @data.setter
    def data(self, value:list):
        self.__data = value

         