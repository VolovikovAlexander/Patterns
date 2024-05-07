import json
from datetime import datetime

from Src.Logics.storage_observer import storage_observer


#
# Класс для обработки и хранения текстовой информации об ошибке
#
class error_proxy:
    " Текст с описание ошибки "
    __error_text = ""
    __log_type:str = ""
    __period: datetime = datetime.now()
    
    def __init__(self, exception: Exception = None):
        if exception is not None:
            self.set_error(exception)

    @property
    def log_type(self) -> str:
        """
            Тип логирования
        Returns:
            str: _description_    
        """
        return self.__log_type     


    @log_type.setter
    def log_type(self, value:str):
        """
            Тип логирования
        Returns:
            str: _description_    
        """    
        self.__log_type = value
          

    @property
    def period(self):
        """
            Дата создания сообщения
        """
        return self.__period
    
    @property
    def error(self):
        """
            Получить текстовое описание ошибки
        Returns:
            str: _description_
        """
        return self.__error_text
    
    @error.setter
    def error(self, value: str):
        if value == "":
            raise Exception("Некорректно переданы параметры!")
            
        self.__error_text = value
        
    @classmethod
    def set_error(self, exception: Exception):
        """
            Сохранить текстовое описание ошибки из исключения
        Args:
            exception (Exception): входящее исключение
        """
        
        if exception  is None:
            self.__error_text = ""
            return
            
        self.__error_text = f"Ошибка! {str(exception)}"    
        error_proxy.write_log(self.__error_text, "ERROR")
        storage_observer.raise_event( "save_log" )

            
    @property        
    def is_empty(self) -> bool:
        """
            Флаг. Есть ошибка
        Returns:
            bool: _description_
        """
        if len(self.__error_text) != 0:
            return False
        else:
            return True       
        
    def clear(self):
        """
            Очистить
        """
        self.__error_text = "" 

    # Фабричные методы   

    @staticmethod    
    def create_error_response( app,  message: str, http_code: int = 0):
        """
            Сформировать структуру response_class для описания ошибки
        Args:
            app (_type_): Flask
            message (str): Сообщение
            http_code(int): Код возврата

        Returns:
            response_class: _description_
        """
        
        if app is None:
            raise Exception("Некорректно переданы параметры!")
        
        if http_code == 0:
            code = 500
        else:
            code = http_code
        
        # Формируем описание        
        json_text = json.dumps({"details" : message}, sort_keys = True, indent = 4,  ensure_ascii = False)  
        error_proxy.write_log(f"Сформирован ответ от сервера. Содержание:\n{json_text}", "ERROR") 
        
        # Формируем результат
        result = app.response_class(
            response =   f"{json_text}",
            status = code,
            mimetype = "application/json; charset=utf-8"
        )    
        
        return result
            
    @staticmethod
    def write_log(message: str, log_type:str = "INFO" ):
        """
            Сформировать сообщение для записи лога
        """
        observer_item = storage_observer.get( storage_observer .log_service_key() )
        if observer_item is not None:
            item = error_proxy()
            item.error = message
            item.log_type = log_type

            observer_item.item = item
            storage_observer.raise_event( "write_log" )
                