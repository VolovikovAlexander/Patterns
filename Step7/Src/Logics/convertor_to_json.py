from Src.Logics.convertor import convertor
from Src.reference import reference
from Src.Models.convertor_match import convertor_match
import json
import uuid

class  convertor_to_json(convertor):
    
    @staticmethod     
    def to_dict(source):
        """_summary_

        Args:
            source (_type_): Любой объект любого типа

        Raises:
            Exception: Передан пустой объект

        Returns:
            dict: Возвращает словарь в качестве ключа используется наименование поля объекта
        """
        if source is None:
            raise Exception("ОШИБКА! Параметр source - пустой!")
        
        attributes = {}
        fields = list(filter(lambda x: not x.startswith("_"), dir(source.__class__)))
        for field in fields:
            object = getattr(source.__class__, field)
            if isinstance(object, property):
                value = object.__get__(source, source.__class__)
                
                # Тип данных UUID
                if isinstance(value, uuid.UUID):
                    attributes[field] = str(value.hex)
                    break
                
                # Тип данных list
                if isinstance(value, list):
                    items = []
                    for item in value:
                        items.append(convertor_to_json.to_dict(item))

                    attributes[field] = items
                    break
                
                # Прочий тип данных
                result = convertor_to_json.to_dict(value)  
                if len(result) == 0:
                    attributes[field] = value  
                else:
                    attributes[field] = result      

        return attributes    
    
    def convert(self, source):
        """
        Производим конвертианию любого типа в указанный

        Args:
            dest (reference): Тип данных от класса reference

        Returns:
            reference: Возвращает объект типа reference
        """
        if not isinstance(source, reference):
            self.error = "Некорректный исходный тип для конвертиации данных!"
            return None
        
        items = convertor_to_json.to_dict(source)
        return json.dumps(items, sort_keys = True, indent = 4)  
      
    
    def get_convertor_matсh(self):
        """
        Формируем структуру для фабрики convertor_factory
        """
        result = convertor_match()
        # Исходный тип
        result.source_type = None
        # Тип преобразования
        result.dest_type  = type("")
        result.convertor = self
        return result