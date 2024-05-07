from Src.Logics.Services.service import service
from Src.Models.event_type import event_type
from Src.Storage.storage import storage
from Src.errors import error_proxy
from Src.exceptions import exception_proxy
from Src.Logics.convert_factory import convert_factory
from Src.Logics.storage_observer import storage_observer

import os
import json
from datetime import datetime

#
# Сервис логирования
#
class log_service(service):

    __log_file: str = "patterns_log"
    __storage: storage = None
    __item:error_proxy = None

    def __init__(self, data: list = None) -> None:
        super().__init__(data)
        self.__storage = storage()
        self.__data = []
        storage_observer.append(self)

    @property
    def item(self) -> error_proxy:
        return self.__item
    
    @item.setter
    def item(self, value: error_proxy):
        exception_proxy.validate(value, error_proxy)
        self.__item = value

    def __observe_save_log(self):
        """
            Сохранить лог и очистить историю
        """
        data = self.__data
        period =  datetime.now().strftime('%Y-%m-%d') 
        file_path = os.path.split(__file__)
        log_file = "%s/%s" % (file_path[0], f"{self.__log_file}_{period}.log")
        try:
            if os.path.exists(log_file):
                os.remove(log_file)

            factory = convert_factory()
            with open(log_file, "w") as write_file: 
                data = factory.serialize( data )
                json_text = json.dumps(data, sort_keys = True, indent = 4, ensure_ascii = False)  
                write_file.write(json_text)

        except Exception as ex:
            raise Exception(f"Ошибка при записи файла {log_file}\n{ex}")        



    def handle_event(self, handle_type: str ):
        """
            Обработать событие
        Args:
            handle_type (str): Ключ
        """
        super().handle_event(handle_type)

        # Добавить запись в лог
        if handle_type == event_type.write_log() and self.__item is not None:
            self.__data.append(self.__item)
            
        # Записать лог в файл и очистить    
        if handle_type == event_type.save_log():
            self.__observe_save_log()    






