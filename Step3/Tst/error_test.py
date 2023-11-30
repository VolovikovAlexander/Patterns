from Src.error_proxy import error_proxy 
import unittest

#
# Набор автотестов для проверки работы класса error_proxy
#
class error_proxy_test(unittest.TestCase):
      
   #
   # Проверить метол set_error с передачей источника ошибки
   #
   def test_set_error_with_source(self):
       # Подготовка
       proxy = error_proxy()
       
       # Действие
       proxy.set_error_source("Test", self)
       
       # Проверки
       print(proxy.error)
       assert proxy.error != ""
       
if __name__ == '__main__':
    unittest.main()   