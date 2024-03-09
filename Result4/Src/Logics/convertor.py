from abc import ABC
from Src.errors import error_proxy
from Src.exceptions import exception_proxy

class convertor(ABC):
    # Инкапсуляци обработки ошибок
    _error: error_proxy = error_proxy()
    # Результат конвертации
    _result = []

    
    def convert(self, field: str, object):
        """
            Сконвертировать объект в словарь
        Args:
            source (_type_): Любой тип данных
        """
        exception_proxy.validate(field, str)
        self._error.clear()
         
        
        
        
        
    
