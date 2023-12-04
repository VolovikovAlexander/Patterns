from Src.Models.group_nomenclature import group_nomenclature
from Src.Models.unit_nomenclature import unit_nomenclature
from Src.Models.nomenclature import nomenclature

# 
# Класс для создания различных элемиентов номенклатуры
#
class nomenclature_factory:
    " Структура для хранения данных "
    _storage = {}
    " Ключ для агрегации номенклатурных групп "
    _group_key = "group_nomenclature"
    " Ключ для агрегации единиц измерения "
    _unit_key = "unit_nomenclature"
    " Ключ для агрегации номенклатуры "
    _nomenclature_key = "nomenclature"

    @staticmethod
    def create_default_nomenclature(storage):
        " Фабричный метод: Создать номенкалутуру по умолчанию "
        
        if storage is None:
            raise Exception("Некорректно паредан параметр storage!")
        
        range_unit = nomenclature_factory.create_default_unit(storage)
        range_group = nomenclature_factory.create_default_group(storage)

        item = nomenclature("Новый")
        item.group = range_group[1]
        item.unit = range_unit[1]
        result = (item.id, item)
        
        # Определяем группу по умолчанию
        items = storage.get(nomenclature_factory._nomenclature_key)
        if items is None:
            storage[nomenclature_factory._nomenclature_key] = []
            storage[nomenclature_factory._nomenclature_key].append(result)
            
        return result

    @staticmethod
    def create_default_group(storage):
        " Фабричный метод: Создать группу номенклатуры по умолчанию"
        
        if storage is None:
            raise Exception("Некорректно паредан параметр storage!")
        
        group =   group_nomenclature("Ингредиенты")
        result =  (group.id, group)   
        
        # Определяем группу по умолчанию
        groups = storage.get(nomenclature_factory._group_key)
        if groups is None:
            storage[nomenclature_factory._group_key] = []
            storage[nomenclature_factory._group_key].append(result)
            
        return result   
    
    @staticmethod
    def create_default_unit(storage):
        " Фабричный метод: Создать единицу измерения по умолчанию"
        if storage is None:
            raise Exception("Некорректно паредан параметр storage!")
        
        unit = unit_nomenclature("кг")
        unit.description = "1 Кг (1000 грамм)"
        result = (unit.id, unit)
        
        # Единицу измерения
        units = storage.get(nomenclature_factory._unit_key)    
        if units is None:
            storage[nomenclature_factory._unit_key] = []
            storage[nomenclature_factory._unit_key].append(result)
            
        return result
