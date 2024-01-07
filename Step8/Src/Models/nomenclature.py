from Src.reference import reference


class nomenclature(reference):
    " Группа номенклатуры "
    _group = None
    " Единица измерения "
    _unit = None
    
    @property
    def group(self):
        " Группа номенклатуры "
        return self._group
    
    @group.setter
    def group(self, value: reference):
        " Группа номенклатуры "
        if value == "":
            self._error.set_error_source("Некорректно указана группа", self)
            
        self._group = value    
    
    @property
    def unit(self):
        " Единица измерения "
        return self._unit
    
    @unit.setter
    def unit(self, value: reference):
        " Единица измерения "
        if value == "":
            self._error.set_error_source("Некорректно указана единица измерения", self)
            
        self._unit = value    