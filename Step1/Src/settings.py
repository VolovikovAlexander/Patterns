#
# Класс для описания настроек
#
class settings():
    _inn = 0
    _short_name = ""
    
    @property
    def inn(self):
        """
            ИНН
        Returns:
            int: 
        """
        return self._inn
    
    @inn.setter
    def inn(self, value: int):
        if not isinstance(value, int):
            raise Exception("Некоррекно переданы параметры!")
        
        self._inn = value
         
    @property     
    def short_name(self):
        """
            Короткое наименование организации
        Returns:
            str:
        """
        return self._short_name
    
    @short_name.setter
    def short_name(self, value:str):
        if not isinstance(value, str):
            raise Exception("Некоррекно переданы параметры!")
        
        self._short_name = value
            
    