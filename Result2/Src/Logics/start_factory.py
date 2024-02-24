from Src.Models.group_model import group_model
from Src.Models.unit_model import unit_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.settings import settings
from Src.Storage.storage import storage
from Src.exceptions import exception_proxy, operation_exception

#
# Класс для обработки данных. Начало работы приложения
#
class start_factory:
    __oprions: settings = None
    __storage: storage = None
    
    def __init__(self, _options: settings,
                 _storage: storage = None) -> None:
        
        exception_proxy.validate(_options, settings)
        self.__oprions = _options
        self.__storage = _storage
        
    
    def __save(self, key:str, items: list):
        """
            Сохранить данные
        Args:
            key (str): ключ доступ
            items (list): список
        """
        exception_proxy.validate(key, str)
        
        if self.__storage == None:
            self.__storage = storage()
            
        self.__storage.data[ key ] = items
        
    @property            
    def storage(self):
        """
             Ссылка на объект хранилище данных
        Returns:
            _type_: _description_
        """
        return self.__storage
    
    # Статические методы
    
    @staticmethod
    def create_units():
        """
            Сформировать список единиц измерения
        Returns:
            _type_: _description_
        """
        items = []
        items.append( unit_model.create_gram())
        items.append( unit_model.create_killogram())
        items.append( unit_model.create_liter())
        items.append( unit_model.create_milliliter())
        items.append(unit_model.create_ting())
        
        return items
    
    @staticmethod
    def create_nomenclatures():
        """
          Сформировать список номенклатуры
        """
        
        group = group_model.create_default_group()
        items = [ {"Мука пшеничная": "киллограмм"}, 
                  {"Сахар":"киллограмм"}, 
                  {"Сливочное масло" : "киллограмм"}, 
                  {"Яйца": "штука"}, {"Ванилин": "грамм"}, 
                  {"Куриное филе": "киллограмм"}, 
                  {"Салат Романо": "грамм"},
                  {"Сыр Пармезан" : "киллограмм"}, 
                  {"Чеснок": "киллограмм"}, 
                  {"Белый хлеб": "киллограмм"},
                  {"Соль": "киллограмм"}, {"Черный перец": "грамм"}, 
                  {"Оливковое масло": "литр"}, 
                  {"имонный сок": "литр"},
                  {"Горчица дижонская": "грамм"},
                  {"Сахарная пудра": "грамм"},{"Ванилиин": "грамм"},
                  {"Корица": "грамм"},
                  {"Какао": "киллограмм"}]
        
        # Подготовим словарь со список единиц измерения
        units = {}
        for position in start_factory.create_units():
            units[ position.name ] = position
        
        result = []
        
        for position in items:
            name   = next(position.keys().__iter__())
            unit_name = next(position.values().__iter__() )
            
            if not unit_name in units.keys():
                raise operation_exception(f"Невозможно найти в списке указанную единицу измерения {unit_name}!")
            
            item = nomenclature_model( name, group, units[unit_name])
            result.append(item)
          
        return result
      
    @staticmethod      
    def create_groups():
        """
            Сформировать список групп номенклатуры
        Returns:
            _type_: _description_
        """
        items = []
        items.append( group_model.create_default_group())
        return items         
    
    def create(self):
        """
           В зависимости от настроек, сформировать или загрузить набор данных
        Returns:
            _type_: _description_
        """
        if self.__oprions.is_first_start == True:
            self.__oprions.is_first_start = False
            
            # 1. Формируем и зпоминаем номеклатуру
            items = start_factory.create_nomenclature()
            self.__save( storage.nomenclature_key(), items )
      
            # 2. Формируем и запоминаем единицы измерения
            items = start_factory.create_units()
            self.__save( storage.unit_key(), items)
            
            # 3. Формируем и запоминаем группы номенклатуры
            items = start_factory.create_groups()
            self.__save( storage.group_key(), items)
           
        else:
            # Другой вариант. Загрузка из источника данных    

        
         return True
    
        
        
        
        
    
    
    
    