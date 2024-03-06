from flask import Flask

app = Flask(__name__)

@app.route("/api/report/<storage_key>", methods = ["GET"]   )
def get_report(storage_key: str):
    
    response_data = app.response_class(
        response = f" ключ {storage_key}",
        status = 200,
        mimetype = "application/text"
    )
    
    return response_data

if __name__ == "__main__":
    app.run(debug = True)