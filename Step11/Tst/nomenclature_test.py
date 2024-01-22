from Db.data_factory import data_factory
from Src.Logics.convertor_factory import convertor_factory
from Src.settings import app_settings
from Src.Logics.convertor_dict_to_reference import convertor_dict_to_reference
from Src.reference import reference

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
        data = {
            "name":"Ингредиенты",
            "description": "Специальная группа для хранения номенклатуры",
            "id": "ef4cbb2a-a318-4f92-b982-66b4278907c6"
            }
        convertor = convertor_dict_to_reference()
        
        # Действие
        result = convertor.convert(data)
        
        # Проверка
        assert result is not None
        
    #
    # Проверить конвертацию из dict в object
    #    
    def test_convert_dict_to_object_factory(self):
        # Подготовка
        data = {
            "name":"Ингредиенты",
            "description": "Специальная группа для хранения номенклатуры",
            "id": "ef4cbb2a-a318-4f92-b982-66b4278907c6"
            }
            
        factory = convertor_factory()
    
        # Действие
        result = factory.convert(data, reference )
        
        # Проверка
        assert result is not None    
        assert result.name == "Ингредиенты"
        assert result.id == "ef4cbb2a-a318-4f92-b982-66b4278907c6"
        assert result.description ==  "Специальная группа для хранения номенклатуры"
    #
    # Проверить загрузку номенклатуры
    #
    def test_load_nomenclature(self):
        # Подготовка
        
        # Действие      
        data_factory.create_nomenclature(self._settings)
        
        # Проверки%
        assert len(data_factory.nomenclature()) >  0    
       
    
    
if __name__ == '__main__':
    unittest.main()      