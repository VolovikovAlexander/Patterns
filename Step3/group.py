from Src.Core.base_models import base_model_name

"""
Модель группы номенклатуры
"""
class group_model(base_model_name):

    """
    Фабричный метод
    """
    @staticmethod
    def create(name: str) -> 'group_model':
        item = group_model()
        item.name = name
        return item
    
    

    


    
