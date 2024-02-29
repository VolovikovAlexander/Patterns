from Src.Logics.reporting import reporting


class csv_reporting(reporting):
    
    def create(self, typeKey: str):
        super().create(typeKey)
        result = ""

        # Исходнеы данные
        items = self.data[ typeKey ]
        
        # Список 
        for field in self.fields:
            result += f"{field};"
        
        # Результат csv
        return result
        
        
        