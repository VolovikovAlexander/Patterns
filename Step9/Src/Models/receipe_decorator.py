from Src.reference import reference

#
# Модель рецепта - декоратор
#
class receipe_decorator(reference):
    # Основная номенклатура   
    _nomenclature = None
    # Состав
    _ingrediens = {}
    
    def __init__(self, nomenclature):
        """
            Конструктор с указанной основной номенклатурой
        Args:
            nomenclature (reference):
        """
        self.nomenclature = nomenclature
        super().__init__(nomenclature.name)
    
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
            Основная номенклатура
        Args:
            value (reference): 
        """
        if value is None:
            raise Exception("Некорректно переданы параметры!")
        
        if not isinstance(value,  reference):
            raise Exception("Некорректный тип данных!")
        
        self._nomenclature = value
        self._name = value.name
        
    @property    
    def is_empty(self):
        """
            Флаг. Пустой состав
        Returns:
            _type_: bool
        """
        if len(self._ingrediens.keys()) == 0:
            return True
        
        return False    
        
    def add(self, nomenclature: reference):
        """
            Добавить в состав ингредиент
        Args:
            nomenclature (reference): Новая номенклатура

        """
        if nomenclature is None:
            raise Exception("Некорректно переданы параметры!")
        
        if not isinstance(nomenclature,  reference):
            raise Exception("Некорректный тип данных!")
        
        if self._nomenclature.id == nomenclature.id:
            raise Exception("Невозможно добавить в состав номенклатуру совпадающую с основной номенклатурой!")
        
        items = list(filter(lambda x: x == nomenclature.id, self._ingrediens.keys()))
        if len(items) != 0:
            raise Exception("Указанная номенклатура уже включена в состав!") 
        
        
        self._ingrediens[nomenclature.id]  = nomenclature     
        
    def delete(self, nomenclature: reference):
        """
            Удалить из состава ингредиент
        Args:
            nomenclature (reference): _description_
  
        """
        if nomenclature is None:
            raise Exception("Некорректно переданы параметры!")
        
        if not isinstance(nomenclature,  reference):
            raise Exception("Некорректный тип данных!")
        
        if self._nomenclature.id == nomenclature.id:
            raise Exception("Невозможно добавить в состав номенклатуру совпадающую с основной номенклатурой!")
        
        items = list(filter(lambda x: x == nomenclature.id, self._ingrediens.keys()))
        if len(items) != 0:
            self._ingrediens.pop(nomenclature.id)
            
                       
        
    