from Db.data_factory import data_factory
from Src.settings import app_settings
from Src.Logics.convertor_dict_to_object import convertor_dict_to_object

import unittest

class nomenclature_test(unittest.TestCase):
    _settings = None
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self._settings = app_settings()
        
    #
    # Проверить работу конвертора из dict в object
    #    
    def test_convert_dict_to_object(self):
        # Подготовка
        data = {}
        convertor = convertor_dict_to_object()
        
        # Действие
        result = convertor.convert(data)
        
        # Проверка
        assert result is not None
        
    
    #
    # Проверить загрузку номенклатуры
    #
    def test_load_nomenclature(self):
        # Подготовка
        
        # Действие      
        data_factory.create_nomenclature(self._settings)
        
        # Проверки%
        assert len(data_factory.nomenclature) >  0    
       
    
    
if __name__ == '__main__':
    unittest.main()      