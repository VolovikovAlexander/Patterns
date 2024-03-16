
from Src.exceptions import argument_exception, exception_proxy, operation_exception
from Src.reference import reference
from Src.Models.storage_model import storage_model
from Src.Models.storage_row_turn_model import storage_row_turn_model

from datetime import datetime

#
# Модель складской проводки
#
class storage_row_model(storage_row_turn_model):
    # Тип складской проводки
    _storage_type: bool = False
    # Период
    _period : datetime
    
    @property
    def storage_type(self) -> bool:
        """
            Тип складской проводки (True - приход, False - расход)
        Returns:
            bool: _description_
        """
        return self._storage_type
    
    @storage_type.setter
    def storage_type(self, value) -> bool:
        """
            Тип складской проводки (True - приход, False - расход)
        Args:
            value (_type_): _description_

        Raises:
            argument_exception: _description_

        Returns:
            bool: _description_
        """
        if isinstance(value, int):
            self._storage_type = True if value > 0 else False
            
        elif isinstance(value, bool):
            self._storage_type = value
            
        else:
            raise argument_exception("Некорректно переданы параметры!")
        
    @property    
    def period(self) -> datetime:
        """
            Дата транзакции
        Returns:
            datetime: _description_
        """
        return self._period
    
    @period.setter
    def period(self, value: datetime) -> datetime:
        """
            Дата транзакции
        """             
        exception_proxy.validate(value, datetime)
        self._period = value
        
    @staticmethod    
    def create_credit_row(nomenclature_name: str, details: list, data: dict, storage: storage_model) -> reference:
        """
            Фабричный метод для создания транзакции на поступление
            Используется в start_factoryu
        Args:
            nomenclature_name (str): Наименование номенклатуры
            details (list): список типа [0.1, "литр"] 
            data (dict): исходный набор данных
            storage(storage_model): склад
        Returns:
            reference: _description_
        """
        exception_proxy.validate(nomenclature_name, str)
        exception_proxy.validate(storage, storage_model)
        if details is None:
            raise argument_exception("Некорректно переданы параметры!")
        
        if len(details) < 2:
            raise argument_exception("Некорректно переданы параметры!")
        
        quantity = details[0]
        unit_name = details[1]
        exception_proxy.validate(quantity, float)
        exception_proxy.validate(unit_name, str)
        
        # Подготовим словарь со списком номенклатуры
        nomenclatures = data[ storage.nomenclature_key() ]    
        
        # Определеяем номенклатуру
        keys = list(filter(lambda x: x == nomenclature_name, nomenclatures.keys() ))
        if len(keys) == 0:
            raise operation_exception(f"Некоректно передан список. Не найдена номенклатура {nomenclature_name}!")
        nomenclature = nomenclatures[keys[0]]    
        
        # Определяем единицу измерения
        units = data[ storage.unit_key()]
        keys = list(filter(lambda x: x == unit_name, units.keys() ))
        if len(keys) == 0:
            raise operation_exception(f"Некорректно передан список. Не найдена единица измерения {unit_name}!")
        unit = units[keys[0]]
        
        
        # Создаем транзакцию
        item = storage_row_model()
        item.nomenclature = nomenclature
        item.unit = unit
        item.storage_type = True
        item.storage = storage
        
        return item
            
        
    
    
    

