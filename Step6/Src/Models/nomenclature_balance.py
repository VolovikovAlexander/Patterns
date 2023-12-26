from Src import reference


#
# Модель для представления информации о балансе номенклатуры
#
class nomenclature_balance(reference):
    # Расходы
    _debit = 0
    # Приходы
    _credit = 0
    # Остаток
    _balance = 0
    
    
    @property
    def debit(self):
        "Все расходы"
        return self._debit
    
    @property
    def credit(self):
        "Все поступления"
        return self._credit
    
    @property
    def balance(self):
        "Текущий остаток"
        return self._balance
    
    
    
    
    

