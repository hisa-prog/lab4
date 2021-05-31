from flask import Flask, Blueprint
from flask_restplus import Api, Resource


from part.part import part_ns as partns1

from list_ import list_np as partns2

from lottery.lottery import lottery_ns as partns3


app = Flask(__name__)

api = Api(app=app)

main_ns = api.namespace('main', description='Main APIs')


@main_ns.route("/")
class MainClass(Resource):

    def get(self):
        return {"status": "Got new data"}

    def post(self):
        return {"status": "Posted new data"}


api.add_namespace(partns1)
api.add_namespace(partns2)
api.add_namespace(partns3)


app.run(debug=True)
