from Src.errors import error_proxy
from Src.Models.storage_row_model import storage_row_model
from datetime import datetime
from Src.exceptions import exception_proxy

#
# Шаблон прототип
#
class storage_prototype(error_proxy):
    # Исходные данные
    __data = []
    
    def __init__(self, data: list[storage_row_model]):
        super().__init__(None)
        if data is None:
            self.error = "Некорректно переданы параметры!"
        else:            
            self.__data = data
        
    @property    
    def data(self):
        """
            Набор складских транзакций
        Returns:
            _type_: _description_
        """
        return self.__data    
        
    
    def filter_period(self, start_period: datetime, stop_period: datetime):
        """
            Фильтр по периоду
        Args:
            start_period (datetime): _description_
            stop_period (datetime): _description_

        Returns:
            storage_prototype : _description_
        """
        self.clear()
        exception_proxy.validate(start_period, datetime)
        exception_proxy.validate(stop_period, datetime)
        
        if len(self.__data) == 0:
            self.error = "Исходные данные пусты!"
            return self.__data
        
        if start_period > stop_period:
            self.error = "Некорректно передан период!"
            return self.__data
        
        result = []
        for item in self.__data:
            if item.period >= start_period and item.period <= stop_period:
                result.append(item)

        return storage_prototype(result)
          