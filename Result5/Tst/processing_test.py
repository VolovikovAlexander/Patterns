import unittest
from Src.Logics.start_factory import start_factory
from Src.settings_manager import settings_manager
from Src.Logics.process_factory import process_factory
from Src.Storage.storage import storage

#
# Набор содульных тестов для проверки процессов обработки данных
#
class processing_test(unittest.TestCase):
    
    #
    # Проверить работу фабрики процессов
    # Запустить расчет складских оборотов
    #
    def test_check_process_factory(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        factory = process_factory()
        key = storage.storage_transaction_key()
        data = start.storage.data[ key ]

        # Действие
        result = factory.create( process_factory.turn_key(), data )
        
        # Проверка
        assert result is not None
    
    
    
   