from flask import Flask

# Подключить Web сервер
app = Flask(__name__)

# Сформировать отчет
@app.route("/report/<storage_key>", methods = ["GET"] )
def get_report(storage_key: str):
    
    # Формируем структуру ответа
    response = app.response_class(
        response = f"** {storage_key} **",
        status = 200,
        mimetype = 'application/text'
    )
    
    return response

if __name__ == "__main__":
    app.run(debug=True)