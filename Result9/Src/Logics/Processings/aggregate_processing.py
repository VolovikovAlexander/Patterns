from Src.Logics.Processings.processing import processing
from Src.Models.receipe_row_model import receipe_row_model
from Src.Storage.storage import storage

#
# Процесс агрегации сохраненных оборотов и рассчитанных
#
class aggregate_processing(processing):
      # Текущие настройки
    __settings: settings = None
    
     
    def __init__(self, exception: Exception = None):
        super().__init__(exception)
        options = settings_manager()
        self.__settings = options.settings
    
    def process(self, source: list) -> list:
        """
            Сформировать агрегацию оборотов
        Args:
            transactions (list): Список полученных оборотов

        Returns:
            list: _description_
        """
        super().process(source)
        
        # Сохране обороты
        object = storage()
        saved_turns = object.data[ storage.blocked_turns_key() ]
        
       
        # Группируем исходные данные 
        grouped_source_data = {}
        for transaction in source:
            key = f"{transaction.nomenclature.id}_{transaction.storage.id}_{transaction.unit.id}"
            if key not in grouped_source_data.keys():
                grouped_source_data[key] = []
                
            grouped_source_data[key].append(transaction)
          
        # Группируем сохраненные данные
        group_saved_data = {}
        for transaction in saved_turns:
            key = f"{transaction.nomenclature.id}_{transaction.storage.id}_{transaction.unit.id}"
            if key not in group_saved_data.keys():
                group_saved_data[key] = []
                
            group_saved_data[key].append(transaction)
            
        # Рассчитывает значения
            
                    

        
        
