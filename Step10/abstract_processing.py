from abc import ABC, abstractmethod
from Src.Core.validator import validator


"""
Абстрактный класс для реализации процесса обработки данных
"""
class abstract_processing(ABC):
    
    @abstractmethod
    def process(self, transactions: list) -> list:
        validator.validate(transactions, list)