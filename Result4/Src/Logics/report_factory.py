from Src.Logics.reporting import reporting
from Src.Logics .markdown_reporting import markdown_reporting
from Src.Logics.csv_reporting import csv_reporting
from Src.exceptions import exception_proxy, argument_exception, operation_exception

#
# Фабрика для отчетов
#
class report_factory:
    __maps = {}
    
    def __init__(self) -> None:
       self.__build_structure()

    def __build_structure(self):
        """
        Сформировать структуру
        """
        self.__maps["csv"]  = csv_reporting
        self.__maps["markdown"] = markdown_reporting
      
      
    def create(self, format: str, data:dict) -> reporting:
        """
            Сформировать объект для построения отчетности
        Args:
            format (str): Тип формта
            data (_type_): Словарь с данными

        Returns:
            reporting: _description_
        """
        exception_proxy.validate(format, str)
        exception_proxy.validate(data, dict)
        
        if len(data) == 0:
            raise argument_exception("Пустые данные")
        
        if format not in self.__maps.keys():
            raise operation_exception(f"Для {format} нет обработчика") 
        
        # Получаем тип связанный с форматом
        report_type = self.__maps[format]
        # Получаем объект 
        result = report_type(data)
        return result 
             
    
      