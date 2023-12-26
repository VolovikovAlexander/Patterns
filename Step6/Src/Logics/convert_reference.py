import abc
from Src.error_proxy import error_proxy
from Src.reference import reference

class convert_reference(error_proxy):
    @abc.abstractmethod
    def convert(self, source, dest):
        if not isinstance(source, reference):
            self.error = "Исходный тип данных - некорректен!"
            return None
        
        if not isinstance(dest, reference):
            self.error = "Тип назначение = некоррекен!"
            return None
        
        
            