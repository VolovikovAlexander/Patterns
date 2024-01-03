from Src.Logics.convertor_to_reference import convertor_to_reference
from Src.Logics.convertor_to_json import convertor_to_json
from Src.Logics.convertor_list_to_json import convertor_list_to_json

#
# Класс для конвертирования данных из одной структуры в другую
#
class convertor_factory:
    
    @staticmethod
    def prepare():
        """
            Подготовить список конверторов
        Returns:
            list: Список конверторов
        """
        _convertors = []
        
        # Конвертор любого объекта в reference
        convertor = convertor_to_reference()
        _convertors.append(convertor.get_convertor_matсh())
        
        # Конвертор любого объекта в json
        convertor = convertor_to_json()
        _convertors.append(convertor.get_convertor_matсh())
        
        # Конвертор массива в json
        convertor = convertor_list_to_json()
        _convertors.append(convertor.get_convertor_matсh())
        
        return _convertors
        
    
    @staticmethod
    def convert(sourceObject, toType):
        """
            Провести конвертацию данных из sourceObject в объект типа toType
        Args:
            sourceObject (reference): Исходный объект для конвертиции
            toType (reference): Тип данных для конвертиации

        Raises:
            - Не найден подходящий конвертор
            - Нет коверторов
            - Ошибка конвертиации данных
        """
        
        _convertors = convertor_factory.prepare()
        if len(_convertors) == 0:
            raise Exception("Список конверторов пуст!")
        
        convertor_match = None
        sort_convertors =  sorted(_convertors, key=lambda x: x.source_type ) 
        for item in _convertors:
            if (item.source_type == None or type(sourceObject) == item.source_type ) and toType ==  item.dest_type:
                convertor_match = item
                
                
        if convertor_match == None:
            raise Exception("Конвертор не определен!")
        
        result = convertor_match.convertor.convert(sourceObject)
        if  convertor_match.convertor.is_error:
            raise Exception( convertor_match.convertor.error)
        
        return result
        
                               
        
        
            
