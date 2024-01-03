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
    result = []
    nomenclature  =  nomenclature_factory._storage.get(nomenclature_factory._nomenclature_key)
    for key, item in nomenclature:
        result.append(item)
        
    return convertor_factory.convert(result, str)



if __name__ == "__main__":
    data_factory.create_nomenclature(100)
    app.run(debug=True)