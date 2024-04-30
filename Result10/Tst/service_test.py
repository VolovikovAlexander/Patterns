from Src.Logics.Services.storage_service import storage_service
from Src.Logics.start_factory import start_factory
from Src.settings_manager import settings_manager
from Src.Storage.storage import storage
from Src.exceptions import operation_exception
from Src.Logics.Services.reference_service import reference_service
from Src.Logics.convert_factory import convert_factory
from Src.Models.nomenclature_model import nomenclature_model
from Src.Logics.storage_observer import storage_observer
from Src.Models.event_type import event_type

from datetime import datetime
import unittest
import uuid

class service_test(unittest.TestCase):
    
    #
    # Тест на удаление номенклатуры
    #
    def test_check_delete_item_reference(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.nomenclature_key()
        data = start.storage.data[ key ]
        if len(data) == 0:
            raise operation_exception("Некорректно сформирован набор данных!")
        service = reference_service(data)
        start_len = len(data)
        item = data[0]
        
        # Действие
        result = service.delete( item )
                
        # Проверки
        assert result == True  
        
    #
    # Тест на удаление номенклатуры из рецепта при удалении карточки номенклатуры
    #    
    def test_check_delere_nomenclature_from_receipt(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.receipt_key()
        receipt_data = start.storage.data[ key ]
        if len(receipt_data) == 0:
            raise operation_exception("Некорректно сформирован набор данных!")
        
        # Номенклатура первая из первого рецепта
        len_receipt_row = len( receipt_data[0].consist )
        receipt_row = receipt_data[0].consist[ list(receipt_data[0].consist.keys())[0] ]
        item = receipt_row.nomenclature
        
        key = storage.nomenclature_key()
        data = start.storage.data[ key ]
        if len(data) == 0:
            raise operation_exception("Некорректно сформирован набор данных!")
        
        service = reference_service(data)
        
        # Действие
        result = service.delete( item ) 
        
        # Проверки
        assert result == True     
        
        key = storage.receipt_key()
        receipt_data = start.storage.data[ key ]
        if len(receipt_data) == 0:
            raise operation_exception("Некорректно сформирован набор данных!")
        
        # Номенклатура первая из первого рецепта
        len_receipt_row_new = len( receipt_data[0].consist )
        
        assert len_receipt_row != len_receipt_row_new
        
        
        
    
    #
    # Проверить добавление reference (номенклатура)
    #
    def test_check_add_item_reference(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.nomenclature_key()
        data = start.storage.data[ key ]
        convert = convert_factory()

        if len(data) == 0:
            raise operation_exception("Некорректно сформирован набор данных!")
        
        # Создаем новый элемент номенклатуры
        dict =  convert.serialize( data[0] )
        item = nomenclature_model().load(dict)
        item.id = uuid.uuid4()

        service = reference_service(data)
        start_len = len(data)

        # Действие
        result = service.add( item )

        # Проверка
        assert result == True
        assert len(data) - 1 == start_len

    # 
    # Проверить изменение reference (номенклатуры)
    #
    def test_check_change_item_reference(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.nomenclature_key()
        data = start.storage.data[ key ]
        convert = convert_factory()

        if len(data) == 0:
            raise operation_exception("Некорректно сформирован набор данных!")
        
        # Создаем новый элемент номенклатуры
        dict =  convert.serialize( data[0] )
        item = nomenclature_model().load(dict)
        item.name = "test"

        service = reference_service(data)
        start_len = len(data)

        # Действие
        result = service.change( item )

        # Проверка
        assert result == True
        assert len(data) == start_len


    #
    # Проверить работу метода create_turns
    #
    def test_check_create_turns(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.storage_transaction_key()
        data = start.storage.data[ key ]
        service = storage_service(data)
        start_date = datetime.strptime("2024-01-01", "%Y-%m-%d")
        stop_date = datetime.strptime("2024-01-10", "%Y-%m-%d")
        
        # Действие
        result = service.create_turns(start_date, stop_date)
        
        # Проверки
        assert len(result) > 0
        
    #
    # Проверить метод     create_turns_by_nomenclature
    #
    def test_check_create_turns_by_nomenclature(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.storage_transaction_key()
        data = start.storage.data[ key ]
        service = storage_service(data)
        start_date = datetime.strptime("2024-01-01", "%Y-%m-%d")
        stop_date = datetime.strptime("2024-01-30", "%Y-%m-%d")
        
        if len(data) == 0:
            raise operation_exception("Набор данных пуст!")
        
        nomenclature = data[0].nomenclature 
        
        # Действие
        result = service.create_turns_by_nomenclature(start_date, stop_date, nomenclature )
        
        # Проверки
        assert len(result) == 1
            
    #
    # Проверить метод  turns_only_nomenclature
    #    
    def test_check_create_turns_only_nomenclature(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.storage_transaction_key()
        data = start.storage.data[ key ]
        service = storage_service(data)
        
        if len(data) == 0:
            raise operation_exception("Набор данных пуст!")
        
        nomenclature = data[0].nomenclature 
        
        # Действие
        result = service.create_turns_only_nomenclature( nomenclature )
        
        # Проверки
        assert len(result) > 0
        
    #
    # Проверить работу метода    create_turns_by_receipt
    # 
    def test_check_create_turns_by_receipt(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.storage_transaction_key()
        transactions_data = start.storage.data[ key ]
        service = storage_service(transactions_data)
        
        if len(transactions_data) == 0:
            raise operation_exception("Набор данных пуст!")
        
        key = storage.receipt_key()
        receipts_data = start.storage.data[ key ]
        
        if len(receipts_data) == 0:
            raise operation_exception("Набор данных пуст!")
        
        receipt = receipts_data[0]
        
        # Действие
        result = service.create_turns_by_receipt(receipt)
        
        # Проверки
        assert len(result) > 0
        
    #
    # Проверить метод  build_debits_by_receipt. Ошибочный сценарий.
    #   
    def test_check_build_debits_by_receipt_fail(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.storage_transaction_key()
        transactions_data = start.storage.data[ key ]
        service = storage_service(transactions_data)
        
        if len(transactions_data) == 0:
            raise operation_exception("Набор данных пуст!")
        
        key = storage.receipt_key()
        receipts_data = start.storage.data[ key ]
        
        if len(receipts_data) == 0:
            raise operation_exception("Набор данных пуст!")
        
        # -> Цезарь с курицей
        receipt = receipts_data[1]
        
        # Действие и проверка
        with self.assertRaises(operation_exception):
            service.build_debits_by_receipt( receipt )
            
            
    #
    # Проверить метод  build_debits_by_receipt. Корректный сценарий
    #   
    def test_check_build_debits_by_receipt_pass(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.storage_transaction_key()
        transactions_data = start.storage.data[ key ]
        start_len_transaction = len(transactions_data)
        service = storage_service(transactions_data)
        
        if len(transactions_data) == 0:
            raise operation_exception("Набор данных пуст!")
        
        key = storage.receipt_key()
        receipts_data = start.storage.data[ key ]
        
        if len(receipts_data) == 0:
            raise operation_exception("Набор данных пуст!")
        
        # -> Вафли хрустящие в вафильнице
        receipt = receipts_data[0]
        
        # Действие и проверка
        service.build_debits_by_receipt( receipt ) 
        stop_len_transaction = len(start.storage.data[  storage.storage_transaction_key() ])
          
        # Проверка (транзакций должно быть больше)   
        assert start_len_transaction < stop_len_transaction   
        
    
    def test_check_observer_blocked_period(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.storage_transaction_key()
        transactions_data = start.storage.data[ key ]
        service = storage_service(transactions_data)
          
        
        # Действие
        try:
            storage_observer.raise_event(  event_type.changed_block_period()  )
            pass
        except Exception as ex:
            print(f"{ex}")
            
        
             
            
        
        