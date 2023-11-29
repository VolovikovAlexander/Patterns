from Src.settings import app_settings 
import unittest


#
# Набор автотестов для проверки работы модуля настроек
#
class settings_test(unittest.TestCase):
    
    #
    # Проверить на корректность создания и загрузки файла с настройками
    #
    def test_create_app_settings(self):
        # Подготовка
        settings = app_settings()

        # Действие
        result = settings.data

        # Проверки
        assert result is not None
        
    #
    # Проверить тип создания объекта как singletone
    #    
    def test_double_create_app_setting(self):
        # Подготовка
        settings1 = app_settings()
        settings2 = app_settings()
        
        # Действие
        
        # Проверки
        print(settings1._uniqueNumber)
        print(settings2._uniqueNumber)
        assert settings1._uniqueNumber == settings2._uniqueNumber
        
        
            

        

 

