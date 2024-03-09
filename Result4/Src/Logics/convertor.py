import abc
from Src.errors import error_proxy
from Src.exceptions import exception_proxy

class convertor(error_proxy):
    
    @abc.abstractmethod
    def convert(self, field: str, object) -> dict:
        """
            Сконвертировать объект в словарь
        Args:
            source (_type_): Любой тип данных
        """
        exception_proxy.validate(field, str)
        self.clear()
         
        
        
        
        
    
