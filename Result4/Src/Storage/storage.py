#
# Класс хранилище данных
#
class storage:
    __data = {}
    
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(storage, cls).__new__(cls)
        return cls.instance  
    
    @property
    def data(self) -> dict:
        """
         Данные по моделям

        Returns:
            _type_: _description_
        """
        return self.__data

 
    @staticmethod
    def nomenclature_key():
        """
            Ключ для хранения номенклатуры
        Returns:
            _type_: _description_
        """
        return "nomenclatures"

  
    @staticmethod
    def group_key():
        """
            Списк номенклатурных групп
        Returns:
            _type_: _description_
        """
        return "groups"
      
      

    @staticmethod  
    def unit_key():
        """
              Список единиц измерения
        Returns:
            _type_: _description_
        """
        return "units"
    
    @staticmethod
    def receipt_key():
        """
            Список рецептов
        Returns:
            _type_: _description_
        """
        return "receipts"
    
    @staticmethod
    def storage_keys():
        """
            Получить список ключей
        """
        return[ storage.group_key(), storage.nomenclature_key(), storage.receipt_key(), storage.unit_key() ]
    