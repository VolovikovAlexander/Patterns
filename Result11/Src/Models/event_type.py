from Src.reference import reference


#
# Типы событий
#
class event_type(reference):
 
    @staticmethod
    def changed_block_period() -> str:
        """
            Событие изменения даты блокировки
        Returns:
            str: _description_
        """
        return "changed_block_period"

    @staticmethod
    def deleted_nomenclature() -> str:
        """
            Событие о удалении номенклатуры
        Returns:
            str: _description_
        """
        return "deleted_nomenclature"

    @staticmethod
    def write_log() -> str:
        """
            Событие - запись в лог
        Returns:
            str: _description_ 
        """
        return "write_log"    
    
    @staticmethod
    def save_log() -> str:
        """
            Событие - сохранить лог
        Returns:
            str: _description_    
        """
        return "save_log"