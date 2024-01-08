import abc
from Src.error_proxy import error_proxy


#
# Абстрактный класс для работы с конвертацией данных
#
class convertor(error_proxy):
    @abc.abstractmethod
    def convert(self, dest):
        """
        Производим конвертианию любого типа в указанный

        Args:
            dest (reference): Тип данных от класса reference

        Returns:
            reference: Возвращает объект типа reference
        """
        
    abc.abstractmethod
    def get_convertor_matсh(self):
        """
        Формируем структуру для фабрики convertor_factory
        """
     
    
    
    