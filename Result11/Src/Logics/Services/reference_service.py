from Src.Logics.Services.service import service
from Src.exceptions import exception_proxy, operation_exception, error_proxy
from Src.reference import reference
from Src.Logics.storage_observer import storage_observer
from Src.Models.event_type import event_type
from Src.Logics.Services.post_processing_service import post_processing_service
from Src.Logics.storage_prototype import storage_prototype

#
# Сервис для выполнения CRUD операций
#
class reference_service(service):

    def __init__(self, data: list) -> None:
        super().__init__(data)
        storage_observer.append(self)
        post_processing_service( self.data )
        
        
    def add(self, item: reference) -> bool:
        """
            Добавить новый элемент
        """
        exception_proxy.validate(item, reference)
        found = storage_prototype(self.data).filter_by_id(item.id)
        if len(found.data) > 0:
            return False
        
        self.data.append(item)
        error_proxy.write_log(f"Добавлен новый объект. Модель {type(item).__name__}", "DEBUG") 

        return True
    
    def delete(self, item:reference) -> bool:
        """
            Удалить элемент
        """
        exception_proxy.validate(item, reference)
        found = storage_prototype(self.data).filter_by_id(item.id)
        if len(found.data) == 0:
            return False
        item = found.data[0]
       
        # Найти нужный наблюдатель и вызвать событие        
        observer_item = storage_observer.get( storage_observer.post_processing_service_key() )
        if observer_item is not None:
            observer_item.item = item
            storage_observer.raise_event(  event_type.deleted_nomenclature()  )    
            
	    # Удалить элемент
        self.data.remove(item)
        error_proxy.write_log(f"Удален объект. Модель {type(item).__name__}", "DEBUG") 
        return True

    def change(self, item:reference) -> bool:
        """
            Изменить элемент
        """
        exception_proxy.validate(item, reference)
        found = storage_prototype(self.data).filter_by_id(item.id)
        if len(found.data) == 0:
            return False
        
        self.delete(found.data[0])
        self.add(item)

        error_proxy.write_log(f"Изменен объект. Модель {type(item).__name__}", "DEBUG") 
        return True
    
    def get(self) -> list:
        """
            Вернуть список 
        """
        return self.data
    
    def get_item(self, id: str) -> reference:
        """
            Вернуть элемент
        """
        exception_proxy.validate(id, str)
        found = storage_prototype(self.data).filter_by_id(id)
        if len(found.data) == 0:
            raise operation_exception(f"Не найден элемент с кодом {id}!")
        
        return found
    
    def handle_event(self, handle_type: str):
        """
            Обработать событие
        Args:
            handle_type (str): _description_
        """
        super().handle_event(handle_type)






