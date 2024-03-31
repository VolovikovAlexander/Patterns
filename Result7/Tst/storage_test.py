import unittest
from Src.Logics.start_factory import start_factory
from Src.settings_manager import settings_manager

class storage_test(unittest.TestCase):
    
    # 
    # Проверить сохранение данных
    #
    def test_save_data(self):
        # Подготовка
        options = settings_manager()
        start = start_factory( options.settings )
        start.create()
        storage = start.storage
        
        # Действие
        result = storage.save()
        
        # Проверки
        assert result == True