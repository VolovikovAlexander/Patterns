from Src.Logics.storage_service import storage_service
from Src.Logics.start_factory import start_factory
from Src.settings_manager import settings_manager
from Src.Storage.storage import storage
from Src.exceptions import operation_exception

from datetime import datetime
import unittest

class service_test(unittest.TestCase):
    
    #
    # Проверить работу метода create_turns
    #
    def test_check_create_turns(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.storage_transaction_key()
        data = start.storage.data[ key ]
        service = storage_service(data)
        start_date = datetime.strptime("2024-01-01", "%Y-%m-%d")
        stop_date = datetime.strptime("2024-01-10", "%Y-%m-%d")
        
        # Действие
        result = service.create_turns(start_date, stop_date)
        
        # Проверки
        assert len(result) > 0
        
    #
    # Проверить метод     create_turns_by_nomenclature
    #
    def test_check_create_turns_by_nomenclature(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.storage_transaction_key()
        data = start.storage.data[ key ]
        service = storage_service(data)
        start_date = datetime.strptime("2024-01-01", "%Y-%m-%d")
        stop_date = datetime.strptime("2024-01-30", "%Y-%m-%d")
        
        if len(data) == 0:
            raise operation_exception("Набор данных пуст!")
        
        nomenclature = data[0].nomenclature 
        
        # Действие
        result = service.create_turns_by_nomenclature(start_date, stop_date, nomenclature )
        
        # Проверки
        assert len(result) == 1
            
        
        
        