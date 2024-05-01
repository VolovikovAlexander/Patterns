import unittest
from Src.settings_manager import settings_manager
from Src.Logics.start_factory import start_factory
from Src.Logics.Services.log_service import log_service

class storage_test(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        log_service()

    #
    # Проверить сохранение данных
    #
    def test_check_save(self):
        # Подготовка
        options = settings_manager()
        start = start_factory(options.settings)
        start.create()
        storage = start.storage

        # Действие
        result = storage.save()

        # Проверки
        assert result == True

    #
    # Проверить загрузку данных
    #    
    def test_check_load(self):
        # Подготовка
        options = settings_manager()
        start = start_factory(options.settings)
        start.create()
        storage = start.storage


        # Действие
        storage.load()

        # Проверки
        assert len(storage.data) > 0

      
