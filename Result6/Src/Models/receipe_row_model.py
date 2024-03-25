from Src.reference import reference
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.unit_model import unit_model
from Src.exceptions import exception_proxy
from Src.Models.storage_row_model import storage_row_model
from Src.Models.storage_model import storage_model

from datetime import datetime

#
# Класс описание одной строки рецепта
#
class receipe_row_model(reference):
    __nomenclature: nomenclature_model = None
    __size: int = 0
    __unit: unit_model = None
    
    def __init__(self, _nomenclature: nomenclature_model, _size: int, _unit: unit_model):
        """

        Args:
            _nomenclature (nomenclature_model): Объект номенклатура
            _size (int): Размер части
            _unit (unit_model): Объект единица измерения
        """
        exception_proxy.validate(_nomenclature, reference)
        exception_proxy.validate(_unit, reference)
         
        self.__nomenclature = _nomenclature
        self.__size = _size
        self.__unit = _unit
        
        super().__init__( f"{_nomenclature.name} , {_unit.name} ")
    
    @property
    def nomenclature(self):
        """
            Номенклатура
        Returns:
            _type_: _description_
        """
        return self.__nomenclature
    
    
    @property
    def size(self):
        """
            Размер

        Returns:
            _type_: _description_
        """
        return self.__size
    
    
    @size.setter
    def size(self, value: int):
        self.__size = value
    
    
    @property    
    def unit(self):
        """
           Единица измерения

        Returns:
            _type_: _description_
        """
        return self.__unit    
    
    
    @staticmethod
    def create_debit_transaction( row, period : datetime, storage: storage_model ) -> storage_row_model:
        """
            Сформировать транзакцию списания
        Args:
            row (receipe_row_model): исходная запись рецепта
            period (datetime): период
            storage (storage_model): склад

        Returns:
            storage_row_model: _description_
        """
        exception_proxy.validate(period , datetime)
        exception_proxy.validate(storage, storage_model)
        
        item = storage_row_model(f"debit transaction")
        item.nomenclature = row.nomenclature
        item.period  = period
        item.storage = storage
        item.storage_type = False
        item.value = row.size
        item.unit = row.unit
        
        return item
        
    