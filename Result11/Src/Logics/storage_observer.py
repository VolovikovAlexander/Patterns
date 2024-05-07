
#
# Наблюдатель для складских операций
#
class storage_observer:
    observers = []
    
    @staticmethod
    def raise_event(handle_event: str):
        """
            Сформировать события
        Args:
            handle_event (str): _description_
        """

        if handle_event.strip() == "":
            return
        
        for object in storage_observer.observers:
            
            if object is not None:
                object.handle_event(handle_event)

    @staticmethod
    def append(item):
        """
            Добавить наблюдателя
        """
        if item is not None:
            found = storage_observer.get( type(item).__name__ )
            if found is None:
                storage_observer.observers.append(item)


    @staticmethod    
    def keys() -> list:
        """
            Получить список ключей наблюдателей
        Returns:
            list: _description_
        """
        result = []
        for item in storage_observer.observers:
            result.append (  type(item).__name__  )
            
        return result    
            
    @staticmethod        
    def get(observer_name: str):
        """
            Получить наблюдателя
        Args:
            observer_name (str): _description_

        Returns:
            _type_: _description_
        """
        
        result = None
        for item in  storage_observer.observers:
            if type(item).__name__ == observer_name:
                result =  item
                break
            
        return result    
                
    @staticmethod            
    def post_processing_service_key() -> str:
        """
            Ключ post_processing_service
        Returns:
            str: _description_
        """
        return "post_processing_service"    

    @staticmethod     
    def log_service_key() -> str:
        """
            Ключ log_service
        Returns:
            str: _description_
        """
        return "log_service"

   