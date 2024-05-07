from Src.Logics.Processings.processing import processing
from Src.Models.receipe_row_model import receipe_row_model
from Src.Storage.storage import storage
from Src.settings import settings
from Src.settings_manager import settings_manager

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
            source (list): Список расчитанных оборотов

        Returns:
            list: _description_
        """
        super().process(source)
        result = []
        
        # Сохране обороты
        storage_object = storage()
        if storage.blocked_turns_key() not in storage_object.data.keys():
            storage_object.data[ storage.blocked_turns_key() ] = []
            
        saved_turns = storage_object.data[ storage.blocked_turns_key() ]
        
       
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
            
        # Рассчитываем значения
        for grouped_source_data_key in grouped_source_data.keys():
            if grouped_source_data_key in group_saved_data.keys():
                # Данные есть и в расчетных оборотах и в сохраненных. Добавляем оборот.
                grouped_source_data[ grouped_source_data_key ].value += group_saved_data[grouped_source_data_key ]
                
        for group_saved_data_key in group_saved_data.keys():
            if group_saved_data_key not in grouped_source_data.keys():
                # В сохраненных данных есть оборот которого нет в расчетных оборотах         
                grouped_source_data[ group_saved_data_key ] = group_saved_data[group_saved_data_key ]
                
        # Формируем результат
        for  key, value in grouped_source_data.items():
            result.append(  value[0] )   
        
        return result    
            
            
            
                    

        
        
