from Src.exceptions import argument_exception, exception_proxy
from Src.Logics.convert_factory import convert_factory
from Src.settings import settings
from Src.settings_manager import settings_manager
from Src.Models.event_type import event_type

from abc import ABC, abstractclassmethod
import json

#
# Общий класс для наследования. Реализация сервисов.
#
class service(ABC):
    # Набор данных для работы
    __data = []
    # Текущие настройки
    __settings: settings = None
    
    def __init__(self, data: list) -> None:
        if len(data) == 0:
            raise argument_exception("Некорректно переданы параметры!")
        
        self.__data = data
        options = settings_manager()
        self.__settings = options.settings

    @property
    def data(self):
        """
            Текущие данные
        Returns:
            _type_: _description_
        """
        return self.__data
    
    @property
    def settings(self) -> settings:
        """
            Текущие настройки
        Returns:
            settings: _description_
        """
        return self.__settings

    @abstractclassmethod
    def handle_event(self, handle_type: str ):
        """
            Обработать событие
        Args:
            handle_type (str): Ключ
        """
        exception_proxy.validate(handle_type, str )
        pass

    # Общие методы для формирования ответа для Web

    def create_response(self, app, data:list = None):
        """
            Сформировать структуру ответа для Web сервера
        """
        inner_data = self.__data if data is None else data
        return service.create_response(app, inner_data)

    @staticmethod
    def create_response( app, data:list):
        """
            Сформировать структуру ответа для Web сервера
        """        
        if app is None:
            raise argument_exception("Некорректно переданы параметры!")
        
        exception_proxy.validate(data, list)

        # Преоброзование
        dest_data = convert_factory().serialize( data )
        json_text = json.dumps( dest_data, sort_keys = True, indent = 4,  ensure_ascii = False)  
   
        # Подготовить ответ    
        result = app.response_class(
            response = f"{json_text}",
            status = 200,
            mimetype = "application/json; charset=utf-8"
        )
        
        return result
    
