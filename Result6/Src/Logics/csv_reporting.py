from Src.Logics.reporting import reporting
from Src.exceptions import operation_exception


#
# Класс - реализация построение данных в формате csv
#
class csv_reporting(reporting):
    
    def create(self, storage_key: str):
        super().create(storage_key)
        result = ""
        delimetr = ";"

        # Исходные данные
        items = self.data[ storage_key ]
        if items == None:
            raise operation_exception("Невозможно сформировать данные. Данные не заполнены!")
        
        if len(items) == 0:
            raise operation_exception("Невозможно сформировать данные. Нет данных!")
        
        # Заголовок 
        header = delimetr.join(self.fields)
        result += f"{header}\n"
        
        # Данные
        for item in items:
            row = ""
            for field in self.fields:
                attribute = getattr(item.__class__, field)
                if isinstance(attribute, property):
                    value = getattr(item, field)
                    if isinstance(value, (list, dict)) or value is None:
                        value = ""
                        
                    row +=f"{value}{delimetr}"
                
            result += f"{row[:-1]}\n"
            
        
        # Результат csv
        return result