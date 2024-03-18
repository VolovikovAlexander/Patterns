from Src.errors import error_proxy
from Src.Logics.process_factory import process_factory
from Src.Models.storage_row_model import storage_row_model
from datetime import datetime

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
        
    
    def filter_period(self, start_period: datetime, stop_period: datetime) -> list[storage_row_model]:
        """
            Фильтр по периоду
        Args:
            start_period (datetime): _description_
            stop_period (datetime): _description_

        Returns:
            list[storage_row_model]: _description_
        """
        if len(self.__data) == 0:
            self.error = "Исходные данные пусты!"
            return self.__data
        
        if start_period < stop_period:
            self.error = "Некорректно передан период!"
            return self.__data
        
        result = list(filter(lambda x : x.period >= start_period and x.period <= stop_period, self.__data ))
        return storage_prototype(result)
          