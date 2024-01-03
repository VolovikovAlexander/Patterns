import abc
from Src.error_proxy import error_proxy


#
# Абстрактный класс для работы с конвертацией данных
#
class convertor(error_proxy):
    @abc.abstractmethod
    def convert(self, dest):
        """
        Производим конвертианию любого типа в указанный

        Args:
            dest (reference): Тип данных от класса reference

        Returns:
            reference: Возвращает объект типа reference
        """
        
    abc.abstractmethod
    def get_convertor_matсh(self):
        """
        Формируем структуру для фабрики convertor_factory
        """
        
    @staticmethod     
    def to_dict(source):
        """
        Сформировать набор ключ / значение из произвольного объекта
        """
        if source is None:
            raise Exception("ОШИБКА! Параметр source - пустой!")
        
        attributes = {}
        fields = list(filter(lambda x: not x.startswith("_"), dir(source.__class__)))
        for field in fields:
            object = getattr(source.__class__, field)
            if isinstance(object, property):
                value = object.__get__(source, source.__class__)
                type_value = type(value)
                yes_json = hasattr(type_value, "to_json")
                
                if yes_json:
                    result = convertor.to_dict(value)
                    if len(result) == 0:
                        attributes[field] = value.to_json()
                    else:    
                        attributes[field] = convertor.to_dict(value)
                else:
                    yes_list = isinstance(value, list)
                    if yes_list:
                        items = []
                        for item in value:
                            items.append(convertor.to_dict(item))

                        attributes[field] = items
                    else:                                  
                        attributes[field] = value    

        return attributes       
    
    
    