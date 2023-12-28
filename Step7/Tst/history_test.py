from Db.data_factory import data_factory
import unittest

#
# Набор автотестов для проверки работы c моделью nomenclature_hostory
#
class history_test(unittest.TestCase):
    #
    # Проверить формирование тестового набора моделей nomenclature_hostory
    #        
    def test_get_nomenclature_history(self):
        # Подготовка
        data_factory.create_nomenclature(100)
        
        # Действия
        items = data_factory.create_history(100)
              
        # Проверки
        assert len(items) > 0    
    
if __name__ == '__main__':
    unittest.main()       
