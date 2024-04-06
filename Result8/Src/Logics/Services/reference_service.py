from Src.Logics.Services.service import service
from Src.exceptions import exception_proxy
from Src.reference import reference

#
# Сервис для выполнения CRUD операций
#
class reference_service(service):

    def add(self, item: reference) -> bool:
        """
            Добавить новый элемент
        """
        exception_proxy.validate(item, reference)
        found = list(filter(lambda x: x.id == item.id , self.data))     
        if len(found) > 0:
            return False
        
        self.data.append(item)
        return True
    
    def delete(self, item:reference) -> bool:
        """
            Удалить элемент
        """
        exception_proxy.validate(item, reference)
        found = list(filter(lambda x: x.id == item.id , self.data))     
        if len(found) == 0:
            return False
        
        self.data.remove(found[0])
        return True

    def change(self, item:reference) -> bool:
        """
            Изменить элемент
        """
        exception_proxy.validate(item, reference)
        found = list(filter(lambda x: x.id == item.id , self.data))     
        if len(found) == 0:
            return False
        
        self.delete(item)
        self.add(item)
        return True
    

    






