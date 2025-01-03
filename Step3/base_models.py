from Src.Core.abstract_model import abstract_model

"""
Базовый класс для наследования с поддержкой сравнения по коду
"""
class base_model_code(abstract_model):

    def __init__(self) -> None:
        super().__init__()

    def set_compare_mode(self, other_object) -> bool:
         return super().set_compare_mode(other_object)
    
    """
    Переопределим десериализацию
    """
    def deserialize(self, data: dict):
        return super().deserialize(data)
    
        
"""
Базовый класс для наследования с поддержкой сравнения по наименованию
"""    
class base_model_name(abstract_model):
    __name:str = ""

    def __init__(self) -> None:
        super().__init__()

    @property
    def name(self) -> str:
        return self.__name.strip()

    @name.setter
    def name(self, value:str):
        self.__name = value

    def set_compare_mode(self, other_object:'base_model_name') -> bool:
        if other_object is  None: return False
        if not isinstance(other_object, base_model_name): return False

        return self.name ==  other_object.name
            
    """
    Переопределим десериализацию
    """
    def deserialize(self, data: dict):
        return super().deserialize(data)
