import json
from Src.exceptions import operation_exception
from Src.Logics.convert_factory import convert_factory

#
# Класс хранилище данных
#
class storage():
    __data = {}
    __storage_file = "storage.json"
    
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
    
    def load(self):
        """
            Загрузить данные из хранилища
        Raises:
            operation_exception: _description_
        """
        try:
            with open(self.__storage_file, "r") as read_file:
                source = json.load(read_file)   
                
                for key in storage.storage_keys(storage):
                    source_data = source[key]
                    source[key] = []
                    
                    for item in source_data:
                        object = key().load( item )
                        source[key].append(object)
                  
        except Exception as ex:
            raise operation_exception(f"Ошибка при чтении файла {self.__storage_file}\n{ex}")
        
        
    def save(self):
        """
            Сохранить данные в хранилище
        Raises:
            operation_exception: _description_
        """
        try:
            factory = convert_factory()
            with open(self.__storage_file, "w") as write_file:
                data = factory.serialize( self.data )
                json_text = json.dumps(data, sort_keys = True, indent = 4, ensure_ascii = False)  
                write_file.write(json)
                
                return True
        except Exception as ex:
            raise operation_exception(f"Ошибка при записи файла {self.__storage_file}\n{ex}")
            
        return False    

 
    @staticmethod
    def nomenclature_key():
        """
            Ключ для хранения номенклатуры
        Returns:
            _type_: _description_
        """
        return "nomenclature_model"

  
    @staticmethod
    def group_key():
        """
            Списк номенклатурных групп
        Returns:
            _type_: _description_
        """
        return "group_model"
      
      
    @staticmethod
    def storage_transaction_key():
        """
            Список складских проводок
        Returns:
            _type_: _description_
        """
        return "storage_row_model"  
    

    @staticmethod  
    def unit_key():
        """
              Список единиц измерения
        Returns:
            _type_: _description_
        """
        return "unit_model"
    
    @staticmethod
    def receipt_key():
        """
            Список рецептов
        Returns:
            _type_: _description_
        """
        return "receipe_model"
    
    # Код взят: https://github.com/UpTechCompany/GitExample/blob/6665bc70c4933da12f07c0a0d7a4fc638c157c40/storage/storage.py#L30
    
    @staticmethod
    def storage_keys(cls):
        """
            Получить список ключей
        Returns:
            _type_: _description_
        """
        keys = []
        methods = [getattr(cls, method) for method in dir(cls) if callable(getattr(cls, method))]
        for method in methods:
            if method.__name__.endswith("_key") and callable(method):
                keys.append(method())
        return keys
    