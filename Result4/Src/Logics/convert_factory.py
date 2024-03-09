from Src.Logics.basic_convertor import basic_convertor
from Src.Logics.datetime_convertor import datetime_convertor
from Src.exceptions import exception_proxy
from Src.reference import reference
from Src.Logics.convertor import convertor

import datetime

#
# Конвертор reference в словарь
#
class reference_convertor(convertor):
    
    def convert(self, field: str, object) -> dict:
        """
            Сконвертировать 
        Args:
            field (str): поле
            object (_type_): значение
        """
        factory = convert_factory()
        super().convert(field, object)
        result = {}

        
        fields = reference.create_fields(object)
        for field in fields:
            value = getattr(object, field)
            dictionary = factory.convert(value)
            
        return None            
    


#
# Фабрика для конвертация данных во вложенный словарь
#
class convert_factory:
    _maps = {}
    
    def __init__(self) -> None:
        self._maps[datetime] = datetime_convertor
        self._maps[dict] = basic_convertor
        self._maps[int] = basic_convertor
        self._maps[str] = basic_convertor
        self._maps[bool] = basic_convertor
        
        # Связка для всех моделей
        for  inheritor in reference.__subclasses__():
            self._maps[inheritor] = reference_convertor
    
        
    def convert(self, object) -> dict:
        fields = reference.create_fields(object)
        result = {}
        
        for field in fields:
            attribute = getattr(object.__class__, field)
            if isinstance(attribute, property):
                
                value = getattr(object, field)
                # Тип данных list
                if isinstance(value, list):
                    items = []
                    for item in value:
                        items.append( self.convert( item ))

                    result[field] = items
                
                # Известный тип данных
                if type(value) in self._maps.keys():
                    convertor = self._maps[ type(value)]()
                    dictionary = convertor .convert( field, value )
                    result[field] = dictionary
          
        return result  
            
            