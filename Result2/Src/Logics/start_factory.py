from Src.Models.group_model import group_model
from Src.Models.unit_model import unit_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.settings import settings

#
# Класс для обработки начало работы приложения
#
class start_factory:
    __oprions: settings = None
    
    def __init__(self, options: settings) -> None:
        self.__oprions = options
    
    @staticmethod
    def create_nomenclature():
        """
          Фабричный метод Создать список номенклатуры
        """
        
        result = []
        
        
        item1 = nomenclature_model("Мука пшеничная")
        item1.group = group_model.create_group()
        item1.unit = unit_model.create_killogram()
        
        result.append(item1)
        
        return result
    
    
    def create(self):
        """
           В зависимости от настроек, сформировать начальную номенклатуру

        Returns:
            _type_: _description_
        """
        if self.__oprions.is_first_start == True:
            self.__oprions.is_first_start = False
            return start_factory.create_nomenclature()
        else:
            items = []
            return items
        
        
    
    
        
        
        
        
    
    
    
    