


from flask import Flask
from flask_cors import CORS
from src.cleanup.cleanup_api.cleanup_api import cleanup_api
from src.file.api.api import file_api
app = Flask(__name__)
CORS(app)  # this enables CORS 

app.register_blueprint(file_api)
app.register_blueprint(cleanup_api)

if __name__ == "__main__":
    app.run(debug=True)
