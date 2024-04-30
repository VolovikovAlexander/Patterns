from Src.Logics.Services.service import service
from Src.Models.event_type import event_type
from Src.Storage.storage import storage
from Src.errors import error_proxy
from Src.exceptions import exception_proxy, operation_exception
import os

#
# Сервис логирования
#
class log_service(service):

    __log_file = "storage.json"
    __storage: storage = None
    __item:error_proxy = None

    def __init__(self, data: list = None) -> None:
        super().__init__(data)
        self.__storage = storage()

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
        file_path = os.path.split(__file__)
        log_file = "%s/%s" % (file_path[0], self.__storage_file)
        if not os.path.exists(log_file):
            raise operation_exception(f"Невозможно загрузить данные! Не найден файл {log_file}")    


    def handle_event(self, handle_type: str ):
        """
            Обработать событие
        Args:
            handle_type (str): Ключ
        """
        super().handle_event(handle_type)

        if handle_type == event_type.write_log() and self.__item is not None:
            key = storage.log_key()
            self.__storage.data[key].append(self.__item)
            
        if handle_type == event_type.save_log():
            self.__observe_save_log()    






