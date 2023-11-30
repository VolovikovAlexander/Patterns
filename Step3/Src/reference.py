import uuid
from abc import ABC
from Src.error_proxy import error_proxy

class reference(ABC):
    " Readonly: Уникальный код "
    _id = None
    " Краткое наименование "
    _name = ""
    " Описание "
    _description = ""
    " Информация об ошибке "
    _error = error_proxy()
    
    def __init__(self, name):
        _id = uuid.uuid4()
        self.name = name
    
    @property
    def name(self):
        "Краткое наименование"
        return self._name
    
    @name.setter
    def name(self, value: str):
        "Краткое наименование"
        if value == "":
            self._error.set_error("Некорректно указано короткое наименование", self)

        if len(value.strip()) > 50:
            self._error.set_error("Некорректно указано короткое наименование. Превышение длины (50 символов)")
                    
        self._name = value.strip()
        
    @property    
    def description(self):
        " Полное наименование "
        return self._description
    
    @description.setter
    def description(self, value: str):
        " Полное наименование "
        if value == "":
            self._error.set_error("Некорректно указано полное наименование", self)
            
        self._description = value.strip()
        
        
    @property
    def id(self):
        " Уникальный код записи "
        return self._id  

    @property
    def is_error(self):
        " Флаг. Есть ошибка "
        return self._error.error != ""     
    
    
                
            
        
    
    
    
    