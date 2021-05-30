from flask import Flask, Blueprint
from flask_restplus import Api, Resource

app = Flask(__name__)

api = Api(app = app)

name_space = api.namespace('main', description='Main APIs')

@name_space.route("/")
class MainClass(Resource):
  def get(self):
    return {"status": "Got new data"}
  def post(self):
    return {"status": "Posted new data"}

from part.part import api as partns1
api.add_namespace(partns1)

from list_ import api as partns3
from list_ import _list as _list
api.add_namespace(partns3)

from part.parttmpl import api as partns2 
from part.parttmpl import templ as templ 

api.add_namespace(partns2) 
app.register_blueprint(templ,url_prefix='/templ')
app.register_blueprint(_list,url_prefix='/')    

app.run(debug=True)