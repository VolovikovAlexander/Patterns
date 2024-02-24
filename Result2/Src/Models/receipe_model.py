from Src.reference import reference
from Src.Models.receipe_row_model import receipe_row_model
from Src.exceptions import exception_proxy 

#
# Класс описание рецепта приготовления блюда
#
class receipe_model(reference):
    # Вес брутто
    _brutto: int = 0
    
    # Вес нетто
    _netto: int = 0

    # Состав рецепта
    _rows = {}    
    
    
    def add(self, row: receipe_row_model):
        """
            Добавить/ изменить состав блюда
        Args:
            row (receipe_row_model): _description_
        """
        exception_proxy.validate(row, receipe_row_model)
        self._rows[row.name] = row
        self.__calc_brutto()
        
    def delete(self, row: receipe_row_model):
        """
            Удалить из состава блюда
        Args:
            row (receipe_row_model): _description_
        """
        exception_proxy.validate(row, receipe_row_model)
        
        if row.name in self._rows.keys():
            self._rows.pop(row.name)
            
        self.__calc_brutto()    
        
    def __calc_brutto(self):
        """
            Перерасчет брутто
        """
        self._brutto = 0
        for position  in self._rows:
            # Получаем свойство size
            self._brutto += self._rows[position].size 
            
    @property         
    def netto(self):
        return self._netto                        
        
    @netto.setter
    def netto(self, value: int):
        """
            Вес нетто
        Args:
            value (int): _description_
        """
        exception_proxy.validate(value, int)
        
        self._netto = value
    