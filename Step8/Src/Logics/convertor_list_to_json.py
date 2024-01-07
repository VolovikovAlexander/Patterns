from Src.Logics.convertor_to_json import convertor_to_json
from Src.Logics.convertor import convertor
from Src.Models.convertor_match import convertor_match
import json

class convertor_list_to_json(convertor):
    
    def convert(self, source):
        """
            Конвертиация данных
        Args:
            source (list): Любой список объектов

        Raises:
            Exception: Некорректно передан параметр!

        Returns:
            str: Json
        """
        if source is None:
            raise Exception("Некорректно передан параметр!")
        
        if not isinstance(source, list):
            raise Exception("Некорректно передан параметр!")
        
        if len(source) == 0:
            raise Exception("Исходный список пуст!")
        
        items = []
        for item in source:
            items.append(convertor_to_json.to_dict(item))
      
        return  json.dumps(items, indent = 4)          
            
            
          
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