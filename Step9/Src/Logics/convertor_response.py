from Src.Logics.nomenclature_factory import nomenclature_factory
from Src.Logics.convertor_factory import convertor_factory
from connexion.lifecycle import ConnexionResponse


#
# Класс для формирования Json данных из исходного  набора содержащего в объекте типа nomenclature_factory
#
class data_rest:
    
    @staticmethod
    def response( key : str):
        """
            Сформировать Json из набора данных содержащихся в объекте типа nomenclature_factory
        Args:
            key (str): Ключ для словаря для получения данных
            app (_type_): Flask

        Returns:
            str: Json
        """
      
        
        if key is None:
            raise Exception("Некорректно передан параметр!")
        
        if key == "":
            raise Exception("Некорректно передан параметр!")
        
        # Формируем входящий набор данных
        result = []
        items  =  nomenclature_factory._storage.get(key)
        
        if len(items) == 0:
            raise Exception("Некорректно передан ключ. Невозможно получить исходный список значений!")
        
        for key, item in items:
            result.append(item)
        
        # Формируем Json данные    
        result = convertor_factory.convert(result, str)
    
        # Формируем структуру ответа
        response = ConnexionResponse(
            body=result,
            status_code=200,
            content_type='application/json'
        )
    
        return response