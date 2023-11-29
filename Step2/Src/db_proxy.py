from Src.db_status_type import db_status_type
from Src.error_proxy import error_proxy
from abc import ABC, abstractmethod


#
# Абстрактный класс для работы с базой данных
#
class db_proxy(ABC):
    " Текущий статус "
    _status = db_status_type.CLOSE
    " Курсор "
    _cursor = None
    " Информация об ошибке "
    _error = None
    
    @classmethod
    @abstractmethod
    def refresh(self):
        " Public: Переоткрыть соединение с базой данных"
        self.__close_data_base()
        self.__open_data_base()


    @property
    def current_status(self):
        " Public: Текущий статус подключения к базу данных"
        return self._status


    @property
    def current_cursor(self):
        " Readonly: Получить текущий курсор для доступа к данным"
        return self._cursor


    @classmethod
    @abstractmethod
    def __open_data_base(self):
        " Private: Открыть соединение с базой данных"

        # Подключение уже установлено
        if self._status == db_status_type.OPEN:
            return False
        
        try:
            self.open_dataExceptionse()
            return True
        except Exception as ex:
            self._error = error_proxy(ex)
            self._status == db_status_type.ERROR
            return False
                

    @abstractmethod        
    def open_data_base(self):
        " Public: Открыть соединение с базой данных"
        pass
    
    @classmethod
    def __close_data_base(self):
        "  Private: Закрыть соединение с базой данных"
        try:
            self._status = db_status_type.CLOSE
            if self._cursor  is  not None:
                self._cursor.close()
            
        finally:
            self._cursor = None  
            
    def error(self):
        " Public: Информация об ошибке "
        return self._error          

    def __del__(self): 
        " Private: Закрыть соединение с базой данных при удалении объекта"           
        self.__close_data_base()


