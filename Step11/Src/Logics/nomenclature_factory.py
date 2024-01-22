from Src.Models.group_nomenclature import group_nomenclature
from Src.Models.unit_nomenclature import unit_nomenclature
from Src.Models.nomenclature import nomenclature

# 
# Класс для создания различных элемиентов номенклатуры
#
class nomenclature_factory:
    _storage = {}
    " Структура для хранения данных "
    
    _group_key = "group_nomenclature"
    " Ключ для агрегации номенклатурных групп "
    
    _unit_key = "unit_nomenclature"
    " Ключ для агрегации единиц измерения "
    
    
    _nomenclature_key = "nomenclature"
    " Ключ для агрегации номенклатуры "
    
    @staticmethod
    def add_nomenclature( item: nomenclature, storage = None):
        """
            Добавить в хранилище элемент номенклатуры
        Args:
            storage (dict): Словарь_
            item (nomenclature): Объект типа nomenclature
        """
        if item is None:
            raise Exception("Некорректно переданы параметры!")
        
        if not isinstance(item, nomenclature):
            raise Exception("Некорректно переданы параметры!")
        
        # Определяем хранилище
        _storage = None
        if storage is not None:
            _storage = storage
        else:
            _storage = nomenclature_factory._storage 
            
        if _storage is None:
            raise Exception("Хранилище номенклатуры не определено!")
        
        items = _storage.get(nomenclature_factory._nomenclature_key)
        if items is None:
            _storage[nomenclature_factory._nomenclature_key] = []
           
        result = (item.id, item)    
        _storage[nomenclature_factory._nomenclature_key].append(result)   
        
              
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
