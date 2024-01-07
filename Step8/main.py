from flask import Flask

from Db.data_factory import data_factory
from Src.Logics.nomenclature_factory import nomenclature_factory
from data_rest import data_rest

app = Flask(__name__)

@app.route('/nomenclature')
def get_nomenclature():
    """
        Получить список номенклатуры
    Returns:
        Json: 
    """
    response = data_rest.response(nomenclature_factory._nomenclature_key, app)
    return response

@app.route('/groups')
def get_nomenclature_groups():
    """
        Получить  список номенклатурных групп
    Returns:
        Json
    """
    response = data_rest.response(nomenclature_factory._group_key, app)
    return response

@app.route('/units')
def get_nomenclature_groups():
    """
        Получить  список единиц измерения
    Returns:
        Json
    """
    response = data_rest.response(nomenclature_factory._unit_key, app)
    return response
    


if __name__ == "__main__":
    # Сформировать произвольный набор данных
    data_factory.create_nomenclature(100)
    app.run(debug=True)