import unittest
from Src.Logics.reporting import reporting
from Src.Models.unit_model import unit_model
from Src.Storage.storage import storage
from Src.Logics.csv_reporting import csv_reporting
from Src.settings_manager import settings_manager
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.group_model import group_model


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
    # Проверить формированеи отчета в csv формате по единицам измерения
    #    
    def test_check_csv_create_unit_key(self):
        # Подготовка
        data = {}
        list = []
        item = unit_model.create_gram()
        list.append(item)
        key = storage.unit_key()
        data[  key  ] = list 
        manager = settings_manager()
        report = csv_reporting( manager.settings , data )
        
        # Действие
        result = report.create( key )
        
        # Проверки
        assert result is not None
        assert len(result) > 0
        
        
    #
    # Проверить формирование отчета в csv формате по номенклатуре
    #           
    def test_check_csv_create_nomenclature_key(self):
        # Подготовка
        data = {}
        list = []
        
        unit = unit_model.create_killogram()
        group = group_model.create_default_group()
        item = nomenclature_model("Тушка бройлера", group, unit )
        list.append(item)
        
        key = storage.nomenclature_key()
        
        data[  key  ] = list 
        manager = settings_manager()
        report = csv_reporting( manager.settings , data )
        
        # Действие
        result = report.create( key )
        
        # Проверки
        assert result is not None
        assert len(result) > 0
        