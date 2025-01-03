from abc import abstractmethod
from Src.Core.abstract_logic import abstract_logic

"""
Абстрактный класс для наследования различных обработчиков связанных файлами
"""
class abstract_manager(abstract_logic):

    """
    Открыть и обработать файл
    """
    @abstractmethod
    def open(self, file_name:str = ""):
        pass

    """
    Сохранить данные в файл
    """    
    @abstractmethod    
    def save(self, file_name:str = "") -> bool:
        pass
