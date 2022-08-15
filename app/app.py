from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config())

db = SQLAlchemy(app)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
  
        data = "hello world"
        return jsonify({'data': data})

if __name__ == '__main__':
    app.run(debug = True)