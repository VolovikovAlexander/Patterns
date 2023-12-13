import datetime
import uuid
from Src.reference import reference

#
# Модель для представления информации о балансе номенклатуры
#
class nomenclature_hostory:
    _nomenclature_code = None
    _turn  = 0
    _period = None
    _comments = ""
    
    @property
    def nomenclature_code(self):
        "Уникальный код номенклатуры"
        return self._nomenclature_code
    
    @nomenclature_code.setter
    def nomenclature_code(self, value: uuid):
        "Уникальный код номенклатуры"
        if value is None:
            raise Exception("Некорректно передан код номенклатуры!")
        
        if not isinstance(value, uuid):
            raise Exception("Некорректно передан код номенклатуры!")
        
        self._nomenclature_code = value

    @property
    def period(self):
        "Период совершения операции"
        return self._period
    
    @period.setter
    def period(self, value: datetime):
        "Период совершения операции"
        if value is None:
            raise Exception("Некорректно передан период выполнения операции!")
        
        if not isinstance(value, datetime):
            raise Exception("Некорректно передан период выполнения операции!")
        
        self._period = value
        
        
        