from Src.exceptions import argument_exception, exception_proxy
from Src.Logics.convert_factory import convert_factory
from abc import ABC
import json

#
# Общий класс для наследования. Реализация сервисов.
#
class service(ABC):
    # Набор данных для работы
    __data = []
    
    def __init__(self, data: list) -> None:
        if len(data) == 0:
            raise argument_exception("Некорректно переданы параметры!")
        
        self.__data = data


    @property
    def data(self):
        return self.__data


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
        data = convert_factory().serialize( data )
        json_text = json.dumps( data, sort_keys = True, indent = 4,  ensure_ascii = False)  
   
        # Подготовить ответ    
        result = app.response_class(
            response = f"{json_text}",
            status = 200,
            mimetype = "application/json; charset=utf-8"
        )
        
        return result
    
