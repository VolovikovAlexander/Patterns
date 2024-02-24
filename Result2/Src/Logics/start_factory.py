# Модели
from Src.Models.group_model import group_model
from Src.Models.unit_model import unit_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.reference import reference
from Src.Models.receipe_model import receipe_model
from Src.Models.receipe_row_model import receipe_row_model

# Системное
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
                  {"Лимонный сок": "литр"},
                  {"Горчица дижонская": "грамм"},
                  {"Сахарная пудра": "грамм"},{"Ванилиин": "грамм"},
                  {"Корица": "грамм"},
                  {"Какао": "киллограмм"}]
        
        # Подготовим словарь со список единиц измерения
        units = reference.create_dictionary(start_factory.create_units())
        
        result = []
        for position in items:
            # Получаем список кортежей и берем первое значение
            _list =  list(position.items())
            if len(_list) < 1:
                raise operation_exception("Невозможно сформировать элементы номенклатуры! Некорректный список исходных элементов!")
            
            tuple = list(_list)[0]
            
            # Получаем неименование номенклатуры и единицы измерения
            if len(tuple) < 2:
                raise operation_exception("Невозможно сформировать элемент номенклатуры. Длина кортежа не корректна!")
            
            name   = tuple[0]
            unit_name = tuple[1]
            
            if not unit_name in units.keys():
                raise operation_exception(f"Невозможно найти в списке указанную единицу измерения {unit_name}!")
            
            # Создаем объект - номенклатура
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
    
    @staticmethod
    def create_receipt(name: str, comments: str, items: list) -> receipe_model:
        """

        Args:
            name (str): Наименование рецепта
            comments (str): Приготовление
            items (list): Состав

        Raises:
            operation_exception: _description_
            operation_exception: _description_

        Returns:
            receipe_model: _description_
        """
        exception_proxy.validate(name, str)
        
        
        # Подготовим словарь со списком номенклатуры
        data = start_factory.create_nomenclatures()
        nomenclatures = reference.create_dictionary(data)    
                
        receipt = receipe_model(name)
        
        for position in items:
            # Получаем список кортежей и берем первое значение
            _list =  list(position.items())
            if len(_list) < 1:
                raise operation_exception("Невозможно сформировать элементы рецепта! Некорректный список исходных элементов!")
            
            tuple = list(_list)[0]
            if len(tuple) < 2:
                raise operation_exception("Невозможно сформировать элемент рецепта. Длина кортежа не корректна!")
            
            nomenclature_name = tuple[0]
            size = tuple[1]
            
            # Определеяем номенклатура
            keys = list(filter(lambda x: x == nomenclature_name, nomenclatures.keys() ))
            if len(keys) == 0:
                raise operation_exception(f"Некоректно передан список. Не найдена номенклатура {nomenclature_name}!")
            
            nomenclature = nomenclatures[nomenclature_name]
            
            # Определяем единицу измерения
            if nomenclature.unit.base_unit is None:
                unit = nomenclature.unit
            else:
                unit = nomenclature.unit.base_unit    
            
            # Создаем запись в рецепте
            row = receipe_row_model(nomenclature, size, unit)
            receipt.add(row)
        
        return receipt
    
    @staticmethod
    def create_receipts():
        result = []
        
        # ВАФЛИ ХРУСТЯЩИЕ В ВАФЕЛЬНИЦЕ
        items = [ {"Мука пшеничная": 100}, {"Сахар": 80}, {"Сливочное масло": 70},
                  {"Яйца": 1} , {"Ванилин": 5 }
                ]
        result.append( start_factory.create_receipt("ВАФЛИ ХРУСТЯЩИЕ В ВАФЕЛЬНИЦЕ", "", items))
        
        # Цезарь с курицей
        items = [ {"Куриное филе": 200}, {"Салат Романо": 50}, {"Сыр Пармезан": 50},
                  {"Чеснок": 10} , {"Белый хлеб": 30 }, {"Соль": 5}, {"Черный перец": 2},
                  {"Оливковое масло": 10}, {"Лимонный сок": 5}, {"Горчица дижонская": 5},
                  {"Яйца": 2}
                ]
        result.append( start_factory.create_receipt("Цезарь с курицей", "", items))
        
        # Безе
        items = [ {"Яйца": 3}, {"Сахарная пудра":180}, {"Ванилиин" : 5}, {"Корица": 5} ,{"Какао": 20} ]
        result.append( start_factory.create_receipt("Безе", "", items))
        return result
        
    
    # Основной метод
    
    def create(self) -> bool:
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
            
            # 4. Формируем и запоминаем рецепты
            items = start_factory.create_receipts()
            self.__save( storage.receipt_key(), items)
           
        else:
            # Другой вариант. Загрузка из источника данных    

        
         return True
    
        
        
        
        
    
    
    
    