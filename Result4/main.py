from flask import Flask
from Src.settings_manager import settings_manager
from Src.Storage.storage import storage
from Src.errors import error_proxy
from Src.Logics.report_factory import report_factory
from Src.Logics.start_factory import start_factory

app = Flask(__name__)

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
    
    if storage_key == "":
        return error_proxy.create_error_response(app, f"Url запроса не корректен!", 400)
    
    if storage_key not in storage.storage_keys():
        return error_proxy.create_error_response(app, f"Некорректный ключ {storage_key}!", 400)
    
    report = report_factory()
    data = start.storage.data
    result = report.create_response( options.settings.report_mode, data, storage_key,  app )       
    return result

if __name__ == "__main__":
    app.run(debug = True)