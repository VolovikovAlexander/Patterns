from Src.Logics.reporting import reporting
from Src.exceptions import operation_exception
from Src.Logics.convert_factory import convert_factory

import json

#
# Формирование отчета в формате json
#
class json_reporting(reporting):
    
      def create(self, storage_key: str):
        super().create(storage_key)
        
         # Исходные данные
        items = self.data[ storage_key ]
        if items == None:
            raise operation_exception("Невозможно сформировать данные. Данные не заполнены!")
        
        if len(items) == 0:
            raise operation_exception("Невозможно сформировать данные. Нет данных!")
        
        factory = convert_factory()
        data = factory.serialize( items )
        result = json.dumps(data, sort_keys = True, indent = 4, ensure_ascii = False)  
        return result
      
      def mimetype(self) -> str:
          return "application/json; charset=utf-8"     
                
        
        
        
    
    