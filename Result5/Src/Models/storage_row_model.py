from Src.Models.storage_row_turn_model import storage_row_turn
from Src.exceptions import argument_exception, exception_proxy

from datetime import datetime

#
# Модель складской проводки
#
class storage_row_model(storage_row_turn):
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
        
    
    
    

