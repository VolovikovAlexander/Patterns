from Src.Logics.convertor import convertor
from datetime import datetime


#
# Конвертор datetime в словарь
#
class datetime_convertor(convertor):
    
    def convert(self, field: str,  object):
        super().convert( field, object)
      
        if not isinstance(object, datetime):
          self._error.error = f"Некорректный тип данных передан для конвертации. Ожидается: datetime. Передан: {type(object)}"
          return None
      
        try:
            return { field: object.strftime('%YYYY-%mm-%dd %HH:%ss') }
        except Exception as ex:
            self.set_error(ex)    
        