from Src.reference import reference
from Src.exceptions import exception_proxy, operation_exception


class nomenclature_model(reference):
    " Группа номенклатуры "
    _group = None
    " Единица измерения "
    _unit = None
    
    
    def __init__(self, name:str, group: reference = None, unit: reference = None):
        """_summary_

        Args:
            name (str): Наименование
            group (reference): Группа
            unit (reference): Единица измерения
        """
        
        if not group is None:
            exception_proxy.validate(group, reference)
            self._group = group
            
        if not unit is None:  
            exception_proxy.validate(unit, reference)  
            self._unit = unit
            
        super().__init__(name)
    
    @property
    def group(self):
        " Группа номенклатуры "
        return self._group
    
    @group.setter
    def group(self, value: reference):
        " Группа номенклатуры "
        exception_proxy.validate(value, reference)
        self._group = value    
    
    @property
    def unit(self):
        " Единица измерения "
        return self._unit
    
    @unit.setter
    def unit(self, value: reference):
        " Единица измерения "
        exception_proxy.validate(value, reference)
        self._unit = value
        
        
    # Фабричные методы
    
    @staticmethod
    def get(nomenclature_name: str, nomenclatures: dict):
        """
            Получить значение элемента номенклатуры из словаря
        Args:
            nomenclature_name (str): наименование
            nomenclatures (dict): исходный словарь storage.data

        Returns:
            nomenclature_model: _description_
        """
        exception_proxy.validate(nomenclature_name, str)
        
        keys = list(filter(lambda x: x == nomenclature_name, nomenclatures.keys() ))
        if len(keys) == 0:
            raise operation_exception(f"Некоректно передан список. Не найдена номенклатура {nomenclature_name}!")
                
        return nomenclatures[keys[0]]
  
    