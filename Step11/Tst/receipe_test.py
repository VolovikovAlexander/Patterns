from Src.Models.receipe_decorator import receipe_decorator
from Src.Models.receipe_item import receipe_item
from Db.data_factory import data_factory


import unittest

class receipe_test(unittest.TestCase):
    
    #
    # Проверить создание пустого рецепта
    #
    def test_create_empty_receipe(self):
        # Подготовка
        data_factory.create_nomenclature(10)
        base =  data_factory.nomenclature()[0]
        
        # Действие      
        item = receipe_decorator(base[1])
        
        # Проверки%
        assert item.is_empty == True
    
    def test_create_not_empty_receipe(self):
         # Подготовка
        data_factory.create_nomenclature(10)
        base =  data_factory.nomenclature()[0]
        item = receipe_decorator(base[1])

        # Действие
        for number in range(2,6):
            ingredient = data_factory.nomenclature()[number]
            row = receipe_item()
            row.gross = 10
            row.net = 8
            row.nomenclature = ingredient[1]
            
            item.add(row)
            
        # Проверки
        assert item.is_empty == False            
    
    
if __name__ == '__main__':
    unittest.main()      