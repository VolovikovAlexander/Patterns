
from Db.data_factory import data_factory
from Src.Logics.nomenclature_factory import nomenclature_factory
from Src.Logics.data_rest import data_rest
from Src.settings import app_settings

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
    response = data_rest.response(nomenclature_factory._nomenclature_key, app)
    return response

@app.route('/nomenclature/groups', methods=['GET'])
def get_nomenclature_groups():
    """
        Получить  список номенклатурных групп
    Returns:
        Json
    """
    response = data_rest.response(nomenclature_factory._group_key, app)
    return response

@app.route('/nomenclature/units', methods=['GET'])
def get_nomenclature_units():
    """
        Получить  список единиц измерения
    Returns:
        Json
    """
    response = data_rest.response(nomenclature_factory._unit_key, app)
    return response
    
if __name__ == "__main__":
    # Сформировать произвольный набор данных
    data_factory.create_nomenclature(settings.data["nomenclature_count"])
    app.add_api("swagger.yaml")
    app.run()