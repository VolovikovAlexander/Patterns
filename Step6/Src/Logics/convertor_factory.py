from Src.Logics.convertor_to_reference import convertor_to_reference


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
        convertor = convertor_to_reference()
        _convertors.append(convertor.get_convertor_matсh())
        
        return _convertors
        
    
    @staticmethod
    def convert( fromtype, toType):
        """
            Провести конвертацию данных из типа fromtype в тип toType
        Args:
            fromtype (reference): Исходный объект для конвертиции
            toType (reference): Тип данных для конвертиации

        Raises:
            - Не найден подходящий конвертор
            - Нет  коверторов
        """
        
        _convertors = convertor_factory.prepare()
        if len(_convertors) == 0:
            raise Exception("Список конверторов пуст!")
        
        convertor_match = None
        for item in _convertors:
            if (item.source_type == None or isinstance(fromtype,item.source_type )) and isinstance(toType,  item.dest_type):
                convertor_match = item
                
                
        if convertor_match == None:
            raise Exception("Конвертор не определен!")
        
                               
        
        
            
