from flask import request, jsonify
from flask import Blueprint

products = Blueprint('products', __name__)

@products.route('/products', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        
        data = "hello world"
        return jsonify({'data': data})