from abc import ABC

#
# Класс для обработки и хранения текстовой информации об ошибке
#
class error_proxy(ABC):
    " Текст с описание ошибки "
    _error_text = ""
    
    def __init__(self, exception: Exception = None):
        super().__init__()
        if exception is not None:
            self.set_error(exception)
    
    @property
    def error(self):
        " Получить текстовое описание ошибки "
        return self._error_text
    
    @error.setter
    def error(self, value: str):
        " Записать текстовое описание ошибки "
        if value == "":
            self._error_text = ""
            return
            
        self._error_text += value
        
    @classmethod
    def set_error(self, exception: Exception):
        " Записать текстовое описание ошибки по исключению"
        if exception  is None:
            self._error_text = ""
            return
            
        self._error_text += "Ошибка! " + str(exception)   
        
    @classmethod    
    def set_error_source(self, message: str, error_source):
        " Записать текстовое описание ошибки с привязкой к источнику"  
        if message == "":
            self._error_text = ""
            return
            
        self._error_text += "%s : Источник: %s" % (message, error_source)    
        
           
            
            
            