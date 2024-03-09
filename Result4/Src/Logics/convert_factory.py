from Src.Logics.basic_convertor import basic_convertor
from Src.Logics.datetime_convertor import datetime_convertor
from Src.exceptions import exception_proxy, operation_exception
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
        return factory.convert(object)
    


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
        # Сконвертируем данные как список
        result = self.__convert_list(object)
        if result is not None:
            return result
        
        result = {}
        fields = reference.create_fields(object)
        
        for field in fields:
            attribute = getattr(object.__class__, field)
            if isinstance(attribute, property):
                value = getattr(object, field)
                
                # Сконвертируем данные как список
                dictionary =  self.__convert_list(value)
                if dictionary is None:
                    # Сконвертируем данные как значение
                    dictionary = self.__convert_item(field, value)
                    
                if len(dictionary) == 1:
                    result[field] =  dictionary[field]
                else:
                    result[field] = dictionary       
          
        return result  
    
    def __convert_item(self, field: str,  source):
        """
            Сконвертировать элемент        
        Args:
            field (str): Наименование поля
            source (_type_): Значение

        Returns:
            dict: _description_
        """
        exception_proxy.validate(field, str)
        if source is None:
            return {field: None}
        
        if type(source) not in self._maps.keys():
            raise operation_exception(f"Не возможно подобрать конвертор для типа {type(source)}")

        convertor = self._maps[ type(source)]()
        dictionary = convertor.convert( field, source )
        
        if not convertor.is_empty:
            raise operation_exception(f"Ошибка при конвертации данных {convertor.error}")
        
        return  dictionary
            
    def __convert_list(self, source) -> list:
        """
            Сконвертировать список
        Args:
            source (_type_): _description_

        Returns:
            dict: _description_
        """
        if not isinstance(source, list):
            return None
        
        items = []
        for item in source:
            items.append( self.__convert_item( item ))  
        
        return items          