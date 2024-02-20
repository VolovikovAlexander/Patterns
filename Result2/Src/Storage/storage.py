

#
# Класс хранилище данных
#
class storage:
    __data = {}
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(storage, cls).__new__(cls)
        return cls.instance  
      
    
    