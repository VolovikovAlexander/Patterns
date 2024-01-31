import os
import json
import uuid


#
# Класс для работы загрузки настроек
#
class settings_manager(object):
    settings_file_name = "settings.json"
    _data = None
    _uniqueNumber = None
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(settings_manager, cls).__new__(cls)
        return cls.instance  
      

    def __init__(self):
        if self._uniqueNumber is None:
            self._uniqueNumber = uuid.uuid4()
            self.open(self.settings_file_name)

    def __open(self):
        " Private: Открыть настройки с наименованием файла по умолчанию "
        file_path = os.path.split(__file__)
        settings_file = "%s/%s" % (file_path[0], self.settings_file_name)
        if not os.path.exists(settings_file):
            raise Exception("ERROR: Невозможно загрузить настройки! Не найден файл %s", settings_file)

        with open(settings_file, "r") as read_file:
            self._data = json.load(read_file)       

    def open(self, file_name):
        " Public: Открыть настройки с указанным наименованием файла настроек "
        self.settings_file_name = file_name
        self.__open()
    
    
    @property    
    def data(self):
        " Public: Получить загруженные данные "
        return self._data    


    