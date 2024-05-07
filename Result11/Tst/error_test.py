from Src.errors import error_proxy 
from Src.Logics.Services.log_service import log_service

import unittest

#
# Набор автотестов для проверки работы класса error_proxy
#
class error_proxy_test(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        log_service()
    
    #
    # Проверить простой сбособ  создания объекта с ошибкой
    #
    def test_create_error_proxy(self):
        # Подготовка
        proxy = error_proxy()
        
        # Действие
        proxy.error = "test"
        
        # Проверка
        assert proxy.error == "test"
        
    def test_create_exception_error_proxy(self):
        # Подготовка
        proxy = error_proxy()
        
        try:
            # Действие
            proxy.error = ""
        except Exception as ex:
            proxy.set_error(ex)
            
        # Проверка
        print(proxy.error)
        assert proxy.error != ""    
            
            
    