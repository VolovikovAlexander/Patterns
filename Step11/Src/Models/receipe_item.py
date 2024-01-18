from Src.reference import reference

#
# Модель элемента рецепта
#
class receipe_item:
    # Номенклатура   
    _nomenclature = None
    # Вес брутто
    _gross = 0
    # Веc нетто
    _net = 0
    
    
    @property
    def gross(self):
        """
            Вес брутто
        Returns:
            int : 
        """
        return self._gross
    
    @gross.setter
    def gross(self, value: int):
        if not isinstance(value, int):
            raise Exception("Некорректно передан параметр!")
        
        if value < 0:
            raise Exception("Некорректно передан параметр!")
        
        self._gross = value
        
    @property
    def net(self):
        """
            Вет нетто
        Returns:
            int : 
        """
        return self._net
    
    @net.setter
    def net(self, value: int):
        if not isinstance(value, int):
            raise Exception("Некорректно передан параметр!")
        
        if value < 0:
            raise Exception("Некорректно передан параметр!")
        
        self._net = value
            
            
    
    @property
    def nomenclature(self):
        """
            Основная номенклатура

        Returns:
            reference: 
        """
        return self._nomenclature
    
    @nomenclature.setter
    def nomenclature(self, value):
        """
            Номенклатура
        Args:
            value (reference): 
        """
        if value is None:
            raise Exception("Некорректно переданы параметры!")
        
        if not isinstance(value,  reference):
            raise Exception("Некорректный тип данных!")
        
        self._nomenclature = value