import unittest
from Src.Logics.reporting import reporting
from Src.Models.unit_model import unit_model
from Src.Storage.storage import storage
from Src.Logics.csv_reporting import csv_reporting
from Src.settings_manager import settings_manager


class reporting_test(unittest.TestCase):
    
    
    #
    # Проверить статический метод build класса reporting
    #
    def test_check_reporting_build(self):
        # Подготовка
        data = {}
        list = []
        item = unit_model.create_gram()
        list.append(item)
        data[  storage.unit_key()  ] = list 
        
        # Дейстие
        result = reporting.build( storage.unit_key(), data )
        
        # Проверки
        assert result is not None
        assert len(result) > 0
        
        
    #
    # Проверить формированеи отчета в csv
    #    
    def test_check_csv_create(self):
        # Подготовка
        data = {}
        list = []
        item = unit_model.create_gram()
        list.append(item)
        data[  storage.unit_key()  ] = list 
        manager = settings_manager()
        report = csv_reporting( manager.settings , data )
        
        # Действие
        result = report.create( storage.unit_key() )
        
        # Проверки
        assert result is not None
        assert len(result) > 0
                
    