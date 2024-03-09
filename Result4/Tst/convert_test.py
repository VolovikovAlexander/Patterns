from Src.Logics.start_factory import start_factory
from Src.Logics.convert_factory import convert_factory

import unittest

class convert_test(unittest.TestCase):
    
    def test_create_convert_units(self):
        # Подготовка
        items = start_factory.create_nomenclatures()
        factory = convert_factory()
        item = items[0]
        
        # Действие
        result = factory.convert(item)
        
        # Проверки
        assert result is not None