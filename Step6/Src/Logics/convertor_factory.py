from Src import reference

#
# Класс для конвертирования данных из одной структуры в другую
#
class convertor_factory:
    @staticmethod
    def convert(fromtype, toType):
        """_summary_

        Args:
            fromtype (reference): Исходный объект для конвертиции
            toType (reference): Тип данных для конвертиации

        Raises:
            Exception: Некорректный тип данных! Необходим наследник от reference
        """
        if not isinstance(fromtype, reference.reference):
            raise Exception("Некорректно указан параметр! Тип /fromType/ должен быть типом унаследованным от /reference/!")
        
        if not isinstance(toType, reference.reference):
            raise Exception("Некорректно указан параметр! Тип /toType/ должен быть типом унаследованным от /reference/!")
            
            
