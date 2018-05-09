__author__ = 'AG00341558'
from flask import Flask,jsonify
app=Flask(__name__)


stores=[{'name':'my wonder store','items':[{'name':'my item','price':15.99}]}]
@app.route('/')
def home():
    return "hello world"

@app.route('/store',methods=['post'])
def create_store():
    pass
@app.route('/getallstore',methods=['get'])
def get_allstore():
    return jsonify({'stores':stores})
@app.route('/getstore/<string:name>',methods=['get'])
def get_store():
    pass
app.run()