from Src.Logics.convertor import convertor
from datetime import datetime


#
# Конвертор datetime в словарь
#
class datetime_convertor(convertor):
    
    def serialize(self, field: str,  object):
        """
            Сериализовать в словарь
        Args:
            field (str): поле
            object (_type_): значение
        """
        super().serialize( field, object)
      
        if not isinstance(object, datetime):
          self._error.error = f"Некорректный тип данных передан для конвертации. Ожидается: datetime. Передан: {type(object)}"
          return None
      
        try:
            return { field: object.strftime('%Y-%m-%d') }
        except Exception as ex:
            self.set_error(ex)    
        
    def deserialize(self, field: str, value: str, object):
        """
            Десериализовать значение
        Args:
            field (str): название поля
            value (str): значение
            object (_type_): исходный объект
        """
        super().deserialize(field, value, object)    
        if value == "":
            return
        
        try:
            date = datetime.strptime(value, "%Y-%m-%d")
            setattr(object, field, date)
        except Exception as ex:
            self.set_error(ex)