from flask import Flask

from Db.data_factory import data_factory
from Src.Logics.nomenclature_factory import nomenclature_factory
from Src.Logics.convertor_factory import convertor_factory

app = Flask(__name__)

@app.route('/nomenclature')
def get_nomenclature():
    result =  nomenclature_factory._storage.get(nomenclature_factory._nomenclature_key)
    items = []
    for key, item in result:
        items.append(item.to_json())
        
    return items



if __name__ == "__main__":
    data_factory.create_nomenclature(100)
    app.run(debug=True)