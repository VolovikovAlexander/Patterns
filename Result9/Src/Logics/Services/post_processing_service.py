from Src.Logics.Services.service import service
from Src.Models.event_type import event_type
from Src.Models.nomenclature_model import nomenclature_model
from Src.exceptions import exception_proxy 
from Src.Logics.storage_observer import storage_observer
from Src.Models.nomenclature_model import nomenclature_model

#
# Пост процессинг для наблюдения за сервисами
#
class post_processing_service(service):
    
    __nomenclature:nomenclature_model = None
      
    def __init__(self, data: list) -> None:
        super().__init__(data)
        storage_observer.observers.append(self)
    
    @property
    def nomenclature(self) -> nomenclature_model:
        return self.__nomenclature
    
    @nomenclature.setter
    def nomenclature(self, source: nomenclature_model):
        exception_proxy.validate(source, nomenclature_model)
        self.__nomenclature = source 
    
    def __observe_deleted_nomenclature(self, object:nomenclature_model):
        """
            Удалить номенклатуру во всех рецептам
        Args:
            object (nomenclature_model): _description_
        """
        exception_proxy.validate(object, nomenclature_model)
        pass     
         
    def handle_event(self,  handle_type:  str):
        """
            Обработать событие
        Args:
            handle_type (str): _description_
        """
        super().handle_event(handle_type)
        
        if handle_type == event_type.deleted_nomenclature:
            self.__observe_deleted_nomenclature(None)
        
        
            