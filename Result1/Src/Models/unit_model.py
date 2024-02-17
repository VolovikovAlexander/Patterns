from Src.reference import reference
from Src.exceptions import exception_proxy, argument_exception

#
# Модель единицы измерения для номенклатуры
#
class unit_model(reference):
    
    # Базовая единица измерения
    __base_unit: reference = None
    
    # Коэффициент пересчета к базовой единице измерения
    __coefficient: int = 1
    
    def __init__(self, name: str, base_unit: reference = None, coefficient: int = 1 ):
        super().__init__(name)
        
        if base_unit != None:
            self.base_unit = base_unit
            
        if coefficient != 1:
            self.coefficient = coefficient    
        
    
    @property
    def base_unit(self):
        """
            Базовая единица измерения
        Returns:
            _type_: _description_
        """
        return self.__base_unit
    
    
    @base_unit.setter
    def base(self, value: reference ):
        exception_proxy.validate(value, reference)
        self.__base_unit = value
        
    
    @property    
    def coefficient(self):
        """
            Коэффициент пересчета
        Returns:
            _type_: _description_
        """
        return self.__coefficient
    
    @coefficient.setter
    def   coefficient(self, value:int):
        exception_proxy.validate(value, int)
        
        if(value <= 0):
            raise argument_exception("Значение коэффициента должно быть > 1!")
        
        self.__coefficient = value  
        
        
        
        
        
    
    