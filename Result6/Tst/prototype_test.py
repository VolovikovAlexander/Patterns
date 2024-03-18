import unittest

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