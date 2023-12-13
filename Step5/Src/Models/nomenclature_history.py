import datetime
import uuid
from Src.reference import reference

#
# Модель для представления информации о балансе номенклатуры
#
class nomenclature_hostory:
    # Код номенклатуры
    _nomenclature_code = None
    # Сумма
    _turn  = 0
    # Период
    _period = None
    # Комментарий
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
    
    @property    
    def turn(self):
        "Сумма движения"
        return self._turn
    
    @turn.setter
    def turn(self, value: float):
        "Сумма движения"
        if value is None:
            raise Exception("Некорректно передана сумма операции!")
        
        if not isinstance(value, float):
            raise Exception("Некорректно передана сумма операции!")
        
        if value == 0:
            raise Exception("Некорректно передана сумма операции!")
            
            
        
        