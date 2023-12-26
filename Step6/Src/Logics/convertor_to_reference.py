from Src.reference import reference
from Src.Models.convertor_match import convertor_match
from Src.Logics.convertor import convertor

#
# Класс конвертор любого типа унаследованного от reference в объект типа reference
#
class convertor_to_reference(convertor):
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
        
        result = reference(source.name)
        if(source.description != ""):
            result.description = source.description
            
        return result      
    
    def get_convertor_matсh(self):
        """
        Формируем структуру для фабрики convertor_factory
        """
        result = convertor_match()
        result.dest_type  = type(reference("convertor"))
        result.convertor = self
        return result
          
        
            