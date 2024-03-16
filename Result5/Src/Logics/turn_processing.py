from Src.Logics.processing import processing
from Src.Models.storage_row_turn_model import storage_row_turn_model


#
# Процесс получения оборотов по списку транзакций
#
class turn_processing(processing):
    
    # Код взят https://github.com/AItEKS/Design-patterns/blob/fc181e58f51419679574d0c701a8894ccd81aa11/Source/Logic/process_storage_turn.py#L8
    
    def process(self, transactions: list) -> list:
        """
            Сформировать складские обороты
        Args:
            transactions (list): Список объектов типа storage_row_model

        Returns:
            list: _description_
        """
        super().process(transactions)
        result = []

        grouped_transactions: dict = {}
        for transaction in transactions:
            key = {transaction.nomenclature, transaction.storage, transaction.unit }
            if key not in grouped_transactions:
                grouped_transactions[key] = []
                
            grouped_transactions[key].append(transaction)

        for key, group in grouped_transactions.items():
            turnover = sum(transaction.value if transaction.storage_type else -transaction.value for transaction in group)

            row = storage_row_turn_model.create( key[0], key[1], key[2])
            row.value = turnover
            
            result.append(row)

        return result
 
  