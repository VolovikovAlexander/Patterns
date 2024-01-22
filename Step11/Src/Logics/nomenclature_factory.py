from Src.Models.nomenclature import nomenclature
from Src.reference import reference

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
    
    #
    # Добавить номенклутуру в хранилище
    #
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
            
        # Добавляем   
        result = (item.id, item)    
        _storage[nomenclature_factory._nomenclature_key].append(result)  
        
        # Добавляем группу
        nomenclature_factory.add_nomenclature_group(item.group, _storage)  
        
    #
    # Добавить группу номенклатуры в хранилище
    #    
    @staticmethod    
    def add_nomenclature_group(item: reference, storage = None):
        """
            Добавить в хранилище элемент группы номенклатуры
        Args:
            storage (dict): Словарь_
            item (reference): Объект типа reference
        """
        if item is None:
            raise Exception("Некорректно переданы параметры!")
        
        if not isinstance(item, reference):
            raise Exception("Некорректно переданы параметры!")
        
        # Определяем хранилище
        _storage = None
        if storage is not None:
            _storage = storage
        else:
            _storage = nomenclature_factory._storage 
            
        if _storage is None:
            raise Exception("Хранилище номенклатуры не определено!")
        
        items = _storage.get(nomenclature_factory._group_key)
        if items is None:
            _storage[nomenclature_factory._group_key] = []
            
        
        # Ищем элемент
        found =  list(filter(lambda x: x == item.id, _storage[nomenclature_factory._group_key]))
        if len(found) > 0:
            _storage[nomenclature_factory._group_key].remove(found[0])
            
        # Добавляем   
        result = (item.id, item)    
        _storage[nomenclature_factory._group_key].append(result)   
                
        
              
