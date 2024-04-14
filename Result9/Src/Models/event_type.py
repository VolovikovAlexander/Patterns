from Src.reference import reference

#
# Класс описание типов событий
#
class event_type(reference):
    
    """
        Событие: смена периода блокировки
    """
    def change_block_period() -> str:
        return "change_block_period"
    