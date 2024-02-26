import random
from Src.Models.nomenclature_history import nomenclature_history
import unittest
import uuid
from random import randrange
from datetime import timedelta, datetime

#
# Набор автотестов для проверки работы c моделью nomenclature_hostory
#
class history_test(unittest.TestCase):
    
    def random_date(start, end):
        "Сформировать произвольную дату между указанными диапазонами "
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)
    
    def get_nomenclature_history():
        "Сформировать набор исторических данных "
        items = []
        keys = ["203be59a-926f-11ee-b9d1-0242ac120002" , "53728856-926f-11ee-b9d1-0242ac120002", "79c9f71e-926f-11ee-b9d1-0242ac120002", "9f1fed2c-926d-11ee-b9d1-0242ac120002" ]
        
        for nomenclature_code in keys:
            item = nomenclature_history()
            item.nomenclature_code = uuid.UUID(nomenclature_code)
            item.period = history_test.random_date(datetime.strptime("2023-12-01", "%Y-%m-%d"),
                                                       datetime.strptime("2024-01-01", "%Y-%m-%d"))
            item.turn = random.uniform(-5, 5)
            items.append(item)
            
        return items    
            
    #
    # Проверить формирование тестового набора моделей nomenclature_hostory
    #        
    def test_get_nomenclature_history(self):
        # Подготовка
        
        # Действия
        items =  history_test.get_nomenclature_history()
              
        # Проверки
        assert len(items) > 0    
    
if __name__ == '__main__':
    unittest.main()       
