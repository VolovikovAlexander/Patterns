from Src.Logics.convertor import convertor
from Src.Models.convertor_match import convertor_match
from Src.reference import reference

#
# Конвертация словаря в объект типа reference
#
class  convertor_dict_to_reference(convertor):
    def convert(self, source):
        """
        Производим конвертацию словарь в указанный тип данных

        Args:
            source (dict): Словарь

        Returns:
            reference: Возвращает объект типа reference
        """
        if not isinstance(source, dict):
            self.error = "Некорректный исходный тип для конвертиации данных!"
            return None
        
        if len(source) == 0:
            self.error = "Исходный объект не корректный! Список ключей пуст."
            return None
        
        # Описание текущих параметров конвертации
        match = self.get_convertor_matсh()
                 
        # Инстанс нужного объекта
        item = match.dest_type()
        
        # Список полей от типа назначения    
        fields = list(filter(lambda x: not x.startswith("_"), dir(item.__class__)))
        
        # Заполняем свойства 
        for field in fields:
            keys = list(filter(lambda x: x == field, source.keys()))
            if len(keys) != 0:
                value = source[field]
                
                # Если обычное свойство - заполняем.
                if not isinstance(value, list) and not isinstance(value, dict):
                    setattr(item, field, value)
                
        return item        
        
    def get_convertor_matсh(self):
        """
        Формируем структуру для фабрики convertor_factory
        """
        result = convertor_match()
        # Исходный тип
        result.source_type = dict
        # Тип преобразования
        result.dest_type  = reference
        result.convertor = self

        return result    
     