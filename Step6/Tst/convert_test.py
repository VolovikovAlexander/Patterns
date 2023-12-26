from Src.Logics.convertor_factory import convertor_factory
from Src.reference import reference
import unittest

#
# Набор автотестов для проверки работы convertor_factory
#
class history_test(unittest.TestCase):
    
    #
    # Проверка конвертации данных на основе простных типов reference
    #
    def test_convert_reference(self):
        #  Подготовка
        source = reference("source")
        dest = reference("dest")
        
        # Действие
        result = convertor_factory.convert(source, dest)
 
        # Проверки
        assert result.name == dest.name
        
        
    
if __name__ == '__main__':
    unittest.main()       