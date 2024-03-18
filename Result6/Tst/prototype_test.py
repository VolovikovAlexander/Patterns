import unittest
from datetime import datetime

from Src.Logics.start_factory import start_factory
from Src.settings_manager import settings_manager
from Src.Logics.storage_prototype import storage_prototype
from Src.Storage.storage import storage

class prototype_test(unittest.TestCase):
    # 
    # Проверить фильтрацию по периоду
    #
    def test_check_filter_period(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.storage_transaction_key()
        data = start.storage.data[key] 
        reposity = storage_prototype( start.storage.data[key] )
        period = max([item.period for item in data])
        
        
        # Действие
        result = reposity.filter_period(period, period)
        
        # Проверки
        assert reposity.is_empty == True
        assert len(result.data) == 1
        
        
    # 
    # Проверить фильтрацию по периоду
    #
    def test_check_filter_period_combo(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.storage_transaction_key()
        data = start.storage.data[key] 
        reposity = storage_prototype( data )
        start_date = datetime.strptime('2024-01-01', '%Y-%m-%d')
        stop_date = datetime.strptime('2024-05-01', '%Y-%m-%d')
        
        
        # Действие
        result = reposity.filter_period(start_date, stop_date)
        
        # Проверки
        assert reposity.is_empty == True
        assert len(result.data) > 0