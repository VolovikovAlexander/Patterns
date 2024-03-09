from Src.Logics.convertor import convertor

#
# Конвертор простых значений в словарь
#
class basic_convertor(convertor):
   
   def convert(self, field: str, object) -> dict:
      super().convert( field, object)
      
      if not isinstance(object, (int, str, bool)):
          self._error.error = f"Некорректный тип данных передан для конвертации. Ожидается: (int, str, bool). Передан: {type(object)}"
          return None
      
      try:
            return { field: object }
      except Exception as ex:
            self._error.set_error(ex)  
            
      return None        
        
    