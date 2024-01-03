from Src.Logics.convertor_to_json import convertor_to_json
from Src.Logics.convertor import convertor
from Src.Models.convertor_match import convertor_match
import json

class convertor_list_to_json(convertor):
    
    def convert(self, source):
        if source is None:
            raise Exception("Некорректно передан параметр!")
        
        if not isinstance(source, list):
            raise Exception("Некорректно передан параметр!")
        
        if len(source) == 0:
            raise Exception("Исходный список пуст!")
        
        result = []
        convertor = convertor_to_json()
        for item in source:
            result.append(convertor.convert(item))
            
        return  json.dumps(result, sort_keys = True, indent = 4)          
            
            
          
    def get_convertor_matсh(self):
        """
        Формируем структуру для фабрики convertor_factory
        """
        result = convertor_match()
        # Исходный тип
        result.source_type = type([])
        # Тип преобразования
        result.dest_type  = type("")
        result.convertor = self
        return result    