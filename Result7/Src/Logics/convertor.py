import abc
from Src.errors import error_proxy
from Src.exceptions import exception_proxy, argument_exception

# 
# Абстрактный класс для наследования.
# Используется для сериализации и десериализации
#
class convertor(error_proxy):
    
    @abc.abstractmethod
    def serialize(self, field: str, object) -> dict:
        """
            Сериализовать объект в словарь
        Args:
            source (_type_): Любой тип данных
        """
        exception_proxy.validate(field, str)
        self.clear()
        
    @abc.abstractmethod    
    def deserialize(self, field: str, value: dict, object):
        """
            Десериализовать элемент в объект
        Args:
            field (str): наименование поля
            value (str): значение
            object (_type_): исходный тип
        """
        
        exception_proxy.validate(field, str)
        if object is None:
            raise argument_exception("Некорректно переданы параметры!")
        
        self.clear()
            
         
        
        
        
        
    
