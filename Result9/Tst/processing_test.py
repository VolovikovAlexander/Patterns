import unittest
from Src.Logics.start_factory import start_factory
from Src.settings_manager import settings_manager
from Src.Logics.process_factory import process_factory
from Src.Storage.storage import storage
from Src.Logics.Processings.processing import processing
from Src.Models.storage_row_turn_model import storage_row_turn_model
from Src.exceptions import operation_exception
from Src.Models.storage_model import storage_model
from Src.Models.unit_model import unit_model

#
# Набор содульных тестов для проверки процессов обработки данных
#
class processing_test(unittest.TestCase):
    
    #
    # Проверить работу фабрики процессов
    # Запустить расчет складских оборотов
    #
    def test_check_process_factory(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        factory = process_factory()

        # Действие
        result = factory.create( process_factory.turn_key() )
        
        # Проверка
        assert result is not None
        
        
    #
    # Проверить работу процесса расчета оборотов
    #    
    def test_check_process_turns(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        factory = process_factory()
        key = storage.storage_transaction_key()
        transactions = start.storage.data[ key ]
        processing = factory.create( process_factory.turn_key() )
        
        # Действие
        result = processing().process(transactions)
        
        # Проверка
        assert result is not None
        assert len(result) > 0   
        turn = list(filter(lambda x: x.nomenclature.name == "Сыр Пармезан", result ))
        assert turn[0].value == 0.5
        
    #
    # Проверить работы агрегирования оборотов. 
    # В сохраненных данных есть оборот которого нет в рассчитанный
    #    
    def test_check_aggregate_turns(self):
        # Подготовка
        default_storage = storage_model.create_default()
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        nomenclatures = start.storage.data[ storage.nomenclature_key()]
        if len(nomenclatures) == 0:
            raise operation_exception("Список номенклатуры пуст!")
        
        #   Создаем тестовый оборот и добавляем его в хранилище
        turn = storage_row_turn_model()
        turn.nomenclature = nomenclatures[0]
        turn.storage = default_storage
        turn.unit = unit_model.create_killogram()
        turn.value = 1
        
        start.storage.data[ storage.blocked_turns_key()  ] = []
        start.storage.data[ storage.blocked_turns_key()  ].append( turn)
        
        #   Получаем процессы агрегации и расчета оборотов
        factory = process_factory()
        aggregate_processing = factory.create( process_factory.aggregate_key() )
        turn_processing = factory.create( process_factory.turn_key() )
        calculated_turns = turn_processing().process( start.storage.data[ storage.storage_transaction_key()  ]    )   
        calculated_len = len(calculated_turns) 
        
        # Действие
        result = aggregate_processing().process( calculated_turns  )
        
        # Проверки
        assert result is not None    
        assert calculated_len + 1 == len(result)
        
    
    
    
   
   