from unittest.case import _AssertRaisesContext
from Src.Logics.convertor_factory import convertor_factory
from Src.reference import reference
from Src.Models.nomenclature_balance import nomenclature_balance
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
      
        
    
if __name__ == '__main__':
    unittest.main()       