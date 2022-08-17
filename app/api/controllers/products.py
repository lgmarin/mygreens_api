from flask import request, jsonify
from . import products

@products.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        
        data = "hello world"
        return jsonify({'data': data})