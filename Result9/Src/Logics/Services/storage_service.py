from Src.Logics.process_factory import process_factory
from Src.Logics.storage_prototype import storage_prototype
from Src.exceptions import argument_exception, exception_proxy, operation_exception
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.receipe_model import receipe_model
from Src.Storage.storage import storage
from Src.Logics.Services.service import service
from Src.Models.event_type import event_type
from Src.Logics.storage_observer import storage_observer
from Src.reference import reference


from datetime import datetime

#
# Сервис для работы со складскими операциями
#
class storage_service(service):
    
    def __init__(self, data: list) -> None:
        super().__init__(data)
        storage_observer.observers.append(self)
    
    def __build_turns(self, data: list) -> list:
        """
            Сформировать обороты
        Args:
            data (list): _description_

        Returns:
            list: _description_
        """
        if len(data) == 0:
            raise argument_exception("Некорректно переданы параметры!")
        
        # Подобрать процессинг    
        key_turn = process_factory.turn_key()
        processing = process_factory().create( key_turn  )
    
        # Обороты
        turns =  processing().process( data )
        return turns
            
    def __build_blocked_turns(self):
        """
            Сформировать и сохранить обороты в закрытом периоде
        """
        start_period = datetime.strptime("1900-01-01", "%Y-%m-%d")   
        stop_period = self.settings.block_period
        
        # Фильтруем по периоду
        prototype = storage_prototype(  self.data )  
        filter = prototype.filter_by_period( start_period, stop_period)
        if len(filter.data) == 0:
            storage().save_blocked_turns( [] )
        else:    
            # Расчитываем 
            calculated_turns = self.__build_turns(filter.data)
        
            # Сохраняем данные
            storage().save_blocked_turns(calculated_turns)
        
    # Набор основных методов    
        
    def create_turns(self, start_period: datetime, stop_period:datetime ) -> list:
        """
            Получить обороты за период
        Args:
            start_period (datetime): Начало
            stop_period (datetime): Окончание

        Returns:
            list: обороты за период
        """
        exception_proxy.validate(start_period, datetime)
        exception_proxy.validate(stop_period, datetime)
        
        if start_period > stop_period:
            raise argument_exception("Некорректно переданы параметры!")
        
        block_period = self.settings.block_period
        
        # Фильтруем      
        prototype = storage_prototype(  self.data )  
        filter = prototype.filter_by_period( block_period, stop_period)
        
        # Рассчитанные обороты
        calculated_turns = self.__build_turns( filter. data )
        
        # Сформируем результат
        aggregate_key = process_factory.aggregate_key()
        processing = process_factory().create( aggregate_key  )
        return processing().process( calculated_turns )
        
    def create_turns_by_nomenclature(self, start_period: datetime, stop_period: datetime, nomenclature: nomenclature_model) -> list:
        """
            Получить обороты за период по конкретной номенклатуры
        Args:
            start_period (datetime): Начало
            stop_period (datetime): Окончание
            nomenclature (nomenclature_model): Номенклатуры

        Returns:
            list: Обороты
        """
        exception_proxy.validate(start_period, datetime)
        exception_proxy.validate(stop_period, datetime)
        exception_proxy.validate(nomenclature, nomenclature_model)
        
        if start_period > stop_period:
            raise argument_exception("Некорректно переданы параметры!")
        
        block_period = self.settings.block_period
        
        # Фильтруем      
        prototype = storage_prototype(  self.data )  
        filter = prototype.filter_by_period( block_period, stop_period)
        filter = filter.filter_by_nomenclature( nomenclature )
        if not filter.is_empty:
            raise operation_exception(f"Невозможно сформировать обороты по указанным данных: {filter.error}")
        
        # Рассчитанные обороты    
        calculated_turns =  self.__build_turns( filter. data )   
        
        # Сформируем результат
        aggregate_key = process_factory.aggregate_key()
        processing = process_factory().create( aggregate_key  )
        return processing().process( calculated_turns ) 
    
    def create_turns_only_nomenclature(self, nomenclature: nomenclature_model) -> list:
        """
            Получить обороты по номенклатуре
        Args:
            nomenclature (nomenclature_model): _description_

        Returns:
            list: Обороты
        """
        exception_proxy.validate(nomenclature, nomenclature_model)
        prototype = storage_prototype(  self.data )  
        filter = prototype.filter_by_nomenclature( nomenclature )
        if not filter.is_empty:
            raise operation_exception(f"Невозможно сформировать обороты по указанным данных: {filter.error}")
         
        return self.__build_turns( filter. data )   
    
    def create_turns_by_receipt(self, receipt: receipe_model) -> list:
        """
            Сформировать обороты по указанному рецепту
        Args:
            receipt (receipe_model): _description_

        Returns:
            list: _description_
        """
        exception_proxy.validate(receipt, receipe_model)
        
        if len(receipt.consist) == 0:
            raise operation_exception("Переданный рецепт некорректный. Не содержит в себе список номенклатуры!")
        
        # Отфильтровать по рецепту
        transactions = []
        filter =  storage_prototype(  self.data )
        for item in receipt.rows():
            filter =  filter.filter_by_nomenclature( item.nomenclature )
            if filter.is_empty:
                for transaction in filter.data:
                    transactions.append( transaction )
                    
            filter.data = self.data        
            
        return self.__build_turns( transactions )     
    
    def build_debits_by_receipt(self, receipt: receipe_model) -> list:
        """
            Сформировать проводки списания по рецепту
        Args:
            receipt (receipe_model): _description_

        Returns:
            list: _description_
        """
        exception_proxy.validate(receipt, receipe_model)
        
        if len(receipt.consist) == 0:
            raise operation_exception("Переданный рецепт некорректный. Не содержит в себе список номенклатуры!")
        
        turns = self.create_turns_by_receipt(receipt)
        if len(turns) <= 0:
            raise operation_exception("По указанному рецепту не найдеты обороты!")
        
        if len(receipt.rows()) > len(turns):
            raise operation_exception("Невозможно сформировать список транзакций для списания т.к. нет достаточно остатков!")
        
        # Формируем список проводок на списание
        processing = process_factory().create( process_factory.debit_key() )
        transactions = processing().process( receipt.rows() )
        key = storage.storage_transaction_key()
        
        data = storage().data[ key ]
        for transaction in transactions:
            data.append ( transaction )
    
    # Набор основных методов   
        
    def handle_event(self,  handle_type:  str):
        """
            Обработать событие
        Args:
            handle_type (str): _description_
        """
        super().handle_event(handle_type)
        
        if handle_type == event_type.changed_block_period():
            self.__build_blocked_turns()
        
    
  