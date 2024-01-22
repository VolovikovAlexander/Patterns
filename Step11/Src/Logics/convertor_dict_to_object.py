from Src.Logics.convertor import convertor
from Src.Models.convertor_match import convertor_match
from Src.reference import reference

#
# Конвертация словаря в указанный объект
#
class  convertor_dict_to_object(convertor):
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
        
        if len(source.keys) == 0:
            self.error = "Исходный объект не корректный! Список ключей пуст."
            return None
        
        # Описание текущих параметров конвертации
        match = self.get_convertor_matсh()

        # Список полей от типа назначения    
        fields = list(filter(lambda x: not x.startswith("_"), dir(match.dest_type.__class__)))
        
        # Инстанс нужного объекта
        item = match.dest_type()
        for field in fields:
            keys = list(filter(lambda x: x == field), source.keys)
            if len(keys) != 0:
                item[field] = source[field]
        
    def get_convertor_matсh(self):
        """
        Формируем структуру для фабрики convertor_factory
        """
        result = convertor_match()
        # Исходный тип
        result.source_type = type(dict)
        # Тип преобразования
        result.dest_type  = type(reference)
        result.convertor = self
        
        self._convertor_math = result
        return result    
     