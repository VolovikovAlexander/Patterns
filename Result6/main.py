from flask import Flask, request
from datetime import datetime
import json

from Src.settings_manager import settings_manager
from Src.Storage.storage import storage
from Src.errors import error_proxy
from Src.Logics.report_factory import report_factory
from Src.Logics.start_factory import start_factory
from Src.Logics.storage_prototype import storage_prototype
from Src.Logics.convert_factory import convert_factory
from Src.Logics.process_factory import process_factory


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# Сформировать начальный набор данных
options = settings_manager() 
start = start_factory(options.settings)
start.create()


@app.route("/api/report/<storage_key>", methods = ["GET"])
def get_report(storage_key: str):
    """
        Сформировать отчет
    Args:
        storage_key (str): Ключ - тип данных: номенклатура, группы и т.д.
    """
    
    keys = storage.storage_keys( start.storage )
    if storage_key == "" or  storage_key not in keys:
        return error_proxy.create_error_response(app, f"Некорректный передан запрос! Необходимо передать: /api/report/<storage_key>. Список ключей (storage_key): {keys}.", 400)
    
    # Создаем фабрику
    report = report_factory()
    data = start.storage.data
    
    # Формируем результат
    try:
        result = report.create_response( options.settings.report_mode, data, storage_key, app )  
        return result
    except Exception as ex:
        return error_proxy.create_error_response(app, f"Ошибка при формировании отчета {ex}", 500)

# http://127.0.0.1:5000//api/storage/turns?start_period=%222023-01-01%22&stop_period=%222024-01-01%22

@app.route("/api/storage/turns", methods = ["GET"])
def get_turns():
    # Фильтруем
    key = storage.storage_transaction_key()
    data = start.storage.data[key]
    prototype = storage_prototype(data)
    args = request.args
    start_period = datetime.strptime(  args.get("start_period", default="", type=str), '%Y-%m-%d')
    stop_period = datetime.strptime( args.get("stop_period", default="", type=str),  '%Y-%m-%d')

    prototype_copy = prototype.filter_period( start_period, stop_period  )
    if not prototype_copy.is_empty:
        return error_proxy.create_error_response(app, f"Ошибка при фильтрации {prototype.error}")
    
    # Расчет оборотов
    factory = process_factory( )
    processing = factory.create( process_factory.turn_key() )
    result = processing().process(prototype_copy.data )
    
    # Конвертация в Json
    convertor = convert_factory()
    data = convertor.serialize( result )
    body = json.dumps(data, sort_keys = True, indent = 4, ensure_ascii = False)  
      
    # Подготовить ответ    
    result = app.response_class(
            response = f"{body}",
            status = 200,
            mimetype =  "application/json; charset=utf-8" 
        )
        
    return result
    
    

if __name__ == "__main__":
    app.run(debug = True)