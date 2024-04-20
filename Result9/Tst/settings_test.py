from Src.settings_manager import settings_manager 
from Src.Logics.start_factory import start_factory
from Src.Logics.Services.storage_service import storage_service
from Src.Storage.storage import storage
import unittest
from datetime import datetime


#
# Набор автотестов для проверки работы модуmeля настроек
#
class settings_test(unittest.TestCase):
    
    # 
    # Проверить действие наблюдателя при изменении даты блокировки
    #
    def test_check_changed_block_period(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.storage_transaction_key()
        transactions_data = start.storage.data[ key ]
        storage_service(transactions_data)
        
        # Действие
        try:
            manager.settings.block_period = datetime.strptime("2024-01-01", "%Y-%m-%d")    
            pass
        except Exception as ex:
            print(f"{ex}")

    #
    # Проверить сохранение настроек
    #
    def test_save_settings(self):
        # Подготовка
        manager = settings_manager()
        manager.settings.block_period = datetime.strptime("2021-02-01", "%Y-%m-%d")

        # Действие
        result = manager.save()

        # Проверки
        assert result == True
        options = settings_manager()
        assert options.settings.block_period == datetime.strptime("2021-02-01", "%Y-%m-%d") 
    
    
    #
    # Проверить на корректность создания и загрузки файла с настройками
    #
    def test_create_app_settings(self):
        # Подготовка
        manager = settings_manager()

        # Действие
        result = manager.data

        # Проверки
        print(manager.data)
        print(type(manager.data))
        assert result is not None
        assert manager.settings.inn > 0
        assert manager.settings.short_name != ""
        
    #
    # Проверить тип создания объекта как singletone
    #    
    def test_double_create_app_setting(self):
        # Подготовка
        manager1 = settings_manager()
        manager2 = settings_manager()
        
        # Действие
        
        # Проверки
        print(manager1._uniqueNumber)
        print(manager2._uniqueNumber)
        assert manager1._uniqueNumber == manager2._uniqueNumber
        
    #
    # Проверить работу менеджера загрузки настроек при не корректном файле настроек
    #    
    def test_fail_open_settings(self):
        # Подготовка
        manager = settings_manager()
        
        # Действие
        manager.open("test.json")
        
        # Проверки
        assert manager.error.is_empty == False
        
        
            

        

 

