from Src.Core.abstract_manager import abstract_manager
from Src.Logics.observe_service import observe_service
from Src.Core.validator import validator, operation_exception
from Src.data_reposity import data_reposity
from Src.Core.convert_factory import convert_factory
from Src.Core.event_type import event_type

import json
import os

"""
Реализация менеджера для записи и загрузки данных по моделям из файла
"""
class file_storage_manager(abstract_manager):
    __file_name = "storage.json"


    # Singletone
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(file_storage_manager, cls).__new__(cls)
        return cls.instance 
    
    def __init__(self):
        super().__init__()
        observe_service.append(self)


    """
    Открыть и загрузить данные
    """
    def open(self, file_name:str = "") -> bool:
        validator.validate(file_name, str)
        
        if file_name != "":
            self.__file_name = file_name

        try:
            current_path_info = os.path.split(__file__)
            current_path = current_path_info[0]
            full_name = f"{current_path}{os.sep}{self.__file_name}"   

            if not os.path.exists(full_name):
                self.set_exception(operation_exception(f"Не найден файл {full_name}!"))
                return False
            else:    
                stream = open(full_name)
                data = json.load(stream) 
                repo = data_reposity()
                repo.clear()
                factory = convert_factory()

                for key in data_reposity.keys():
                    source_data = data [ key ]
                    if source_data is not None:
                        # Создаем модели. Наименование модели совпадаем с наименованием ключа
                        instance = eval( key )
                        # Десериализуем
                        factory.deserialize( source_data, instance)
                        repo.data [ key ] = instance

            return True
        except Exception as ex :
            self.set_exception(ex)
            return False    


    """
    Сохранить данные в файл
    """
    def save(self, file_name:str = "") -> bool:
        if file_name != "":
            self.__file_name = file_name

        try:
            factory = convert_factory()
            repo = data_reposity()
            current_path_info = os.path.split(__file__)
            current_path = current_path_info[0]
            full_name = f"{current_path}{os.sep}{self.__file_name}"   

            if os.path.exists(full_name):
                os.remove(full_name)

            # Готовим Josn
            result = factory.serialize( repo.data )
            json_text = json.dumps(result, sort_keys = True, indent = 4, ensure_ascii = False)  
         
            # Записываем в файл
            with open(full_name, "w") as file:
                file.write(json_text)

            return True
        except Exception as ex :
            self.set_exception(ex)
            return False    
        

    """
    Перегрузка абстрактного метода
    """
    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)

    """
    Перегрузка абстрактного метода
    """
    def handle_event(self, type: event_type, params ):
        super().handle_event(type, params)       

        if type == event_type.LOAD_DATA:
            self.open(self.__file_name)    

        if type == event_type.SAVE_DATA:
            self.save(self.__file_name)


