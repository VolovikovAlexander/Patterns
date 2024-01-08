from unittest.case import _AssertRaisesContext
from Src.Logics.convertor_factory import convertor_factory
from Src.reference import reference
from Src.Models.nomenclature_balance import nomenclature_balance
from Src.Models.nomenclature import nomenclature
from Src.Models.group_nomenclature import group_nomenclature
import unittest

#
# Набор автотестов для проверки работы convertor_factory
#
class convert_test(unittest.TestCase):
    
    #
    # Проверка конвертации данных на основе простных типов reference
    #
    def test_convert_reference(self):
        #  Подготовка
        source = reference("source")
        dest =  type(reference("convertor"))
        
        # Действие(
        result = convertor_factory.convert(source, dest)
 
        # Проверки
        assert result.name == source.name
        
    #
    # Попробовать ошибочно провести конвертиацию типа данных из nomenclature_balance в reference 
    #  
    def test_convert_nomenclature_balance_fail(self):
        #  Подготовка
        source = nomenclature_balance()
        dest =  type(reference("convertor"))
        
        # Действие
        with self.assertRaises(Exception):
            result = convertor_factory.convert(source, dest)
            
    #
    # Попробовать сконвертировать в Json номенклатуру
    #        
    def test_convert_nomenctature_to_json(self):
        # Подготовка
        source = nomenclature("test")
        source.group = group_nomenclature("test")
        
        # Действие
        result =  convertor_factory.convert(source, str)
        
        # Проверка
        print(result)
        assert result is not None
        
    #
    # Попробовать сконвертировать в Json список
    #    
    def test_convert_list_to_json(self):
        # Подготовка
        source = nomenclature("test")
        source.group = group_nomenclature("test")
        items = []
        items.append(source)
        
        # Действие
        result =  convertor_factory.convert(items, str)
        
        # Проверка
        print(result)
        assert result is not None      
            
               
      
        
    
if __name__ == '__main__':
    unittest.main()       