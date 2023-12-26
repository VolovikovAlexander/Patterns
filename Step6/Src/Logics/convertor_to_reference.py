from Src.reference import reference
from Src.Models.convertor_match import convertor_match
from Src.Logics.convertor import convertor

#
# Класс конвертор любого типа унаследованного от reference в объект типа reference
#
class convertor_to_reference(convertor):
    def convert(self, dest):
        """
        Производим конвертианию любого типа в указанный

        Args:
            dest (reference): Тип данных от класса reference

        Returns:
            reference: Возвращает объект типа reference
        """
        if not isinstance(dest, reference):
            self.error = "Некорректный тип назначения для конвертиации данных!"
            return None
        
        result = reference(dest.name)
        result.description = dest.description
        return result      
    
    def get_convertor_matсh(self):
        """
        Формируем структуру для фабрики convertor_factory
        """
        result = convertor_match()
        result.dest_type = type(reference)
        result.convertor = self
        return result
          
        
            