from flask import Flask

from Db.data_factory import data_factory
from Src.Logics.convertor_factory import convertor_factory
from Src.Logics.nomenclature_factory import nomenclature_factory

app = Flask(__name__)

@app.route('/nomenclature')
def get_nomenclature():
    """
        Получить список номенклатуры
    Returns:
        Json: 
    """
    
    # Формируем входящий набор данных
    result = []
    nomenclature  =  nomenclature_factory._storage.get(nomenclature_factory._nomenclature_key)
    for key, item in nomenclature:
        result.append(item)
        
    # Формируем Json данные    
    result = convertor_factory.convert(result, str)
    
    # Формируем структуру ответа
    response = app.response_class(
        response=result,
        status=200,
        mimetype='application/json'
    )
    
    return response


if __name__ == "__main__":
    data_factory.create_nomenclature(100)
    app.run(debug=True)