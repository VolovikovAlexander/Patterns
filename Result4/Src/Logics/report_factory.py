from Src.Logics.reporting import reporting
from Src.Logics.markdown_reporting import markdown_reporting
from Src.Logics.csv_reporting import csv_reporting
from Src.settings import settings
from Src.exceptions import exception_proxy, operation_exception

#
# Класс - фабрика для создание отчетов
#
class report_factory:
    # Настройки
    _settings : settings = None
    
    # Связка
    _maps = {}
    
    def __init__(self, _settings: settings ) -> None:
        exception_proxy.validate(_settings, settings)
        
        self._settings = _settings
        self._maps["csv"] = csv_reporting
        self._maps["markdown"] = markdown_reporting
        
    
    def create(self, data: dict) -> reporting:
        """
            Сформировать произвольный оперативный отчет
        Args:
            data (dict): Источник данных
        Returns:
            reporting: Наследник для формирования нужного отчета
        """
        
        if  self._settings.report_mode in self._maps.keys():
            result = self._maps[self._settings.report_mode](data)
        else:
            raise operation_exception(f"Не найдена обработка для формата {self._settings.report_mode}! Невозможно сформировать отчет!")
            
        return result
            
    
    