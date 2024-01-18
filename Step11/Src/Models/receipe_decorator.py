from Src.reference import reference
from Src.Models.receipe_item import receipe_item

#
# Модель рецепта - decorator
#
class receipe_decorator(reference):
    # Основная номенклатура   
    _nomenclature = None
    # Состав
    _ingrediens = {}
    # Вес брутто
    _gross = 0
    # Вет нетто
    _net = 0
    
    
    def __init__(self, nomenclature):
        """
            Конструктор с указанной основной номенклатурой
        Args:
            nomenclature (reference):
        """
        self.nomenclature = nomenclature
        super().__init__(nomenclature.name)
        
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
        
    def add(self, value: receipe_item):
        """
            Добавить в состав ингредиент и его вес
        Args:
            nomenclature (reference): Новая номенклатура

        """
        if value is None:
            raise Exception("Некорректно переданы параметры!")
        
        if not isinstance(value,  receipe_item):
            raise Exception("Некорректный тип данных!")
        
        if self._nomenclature.id == value.nomenclature.id:
            raise Exception("Невозможно добавить в состав номенклатуру совпадающую с основной номенклатурой!")
        
        items = list(filter(lambda x: x == value.nomenclature.id, self._ingrediens.keys()))

        # TODO: В случае, если указанный ингредиент есть, то необходимо заменить брутто / нетто!
        if len(items) != 0:
            raise Exception("Указанная номенклатура уже включена в состав!") 
        
        self._ingrediens[value.nomenclature.id]  = value     
        
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
            
                       
        
    