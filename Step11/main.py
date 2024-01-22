
from Src.Logics.nomenclature_factory import nomenclature_factory
from Db.data_factory import data_factory
from Src.settings import app_settings
from Src.Logics.convertor_response import convertor_response

import connexion

app = connexion.FlaskApp(__name__, specification_dir='./')
settings = app_settings()
 

@app.route('/nomenclature', methods=['GET'])
def get_nomenclature():
    """
        Получить список номенклатуры
    Returns:
        Json: 
    """
    response = convertor_response.response(nomenclature_factory._nomenclature_key)
    return response

@app.route('/nomenclature/groups', methods=['GET'])
def get_nomenclature_groups():
    """
        Получить  список номенклатурных групп
    Returns:
        Json
    """
    response = convertor_response.response(nomenclature_factory._group_key)
    return response

@app.route('/nomenclature/units', methods=['GET'])
def get_nomenclature_units():
    """
        Получить  список единиц измерения
    Returns:
        Json
    """
    response = convertor_response.response(nomenclature_factory._unit_key)
    return response
    
if __name__ == "__main__":
    # Сформировать произвольный набор данных
    data_factory.create_nomenclature(settings)
    app.add_api("swagger.yaml")
    app.run()