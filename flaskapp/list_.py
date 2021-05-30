from flask import Blueprint
from flask_restplus import fields, Resource, reqparse, Namespace
from random import random
reqp = reqparse.RequestParser()

_list = Blueprint('list', __name__,
                  template_folder='templates', static_folder='static')

api = Namespace('list', description='some information')

list_ = api.model('list',
                  {
                      'len': fields.String(required=True, description='Size of array'),
                      'array': fields.List(fields.String, required=True, description='Some array'),
                  })

allarray = ['1']
# name_space1 = api.namespace('list', description='list APIs')
name_space1 = api


@name_space1.route("/")
class ListClass(Resource):
    @name_space1.doc("")
    @name_space1.marshal_with(list_)
    def get(self):
        """"Получение всего хранимого массива"""
        return {'len': str(len(allarray)), 'array': allarray}

    @name_space1.doc("")
    @name_space1.expect(list_)
    @name_space1.marshal_with(list_)
    def post(self):
        """Создание массива/наше описание функции пост"""
        global allarray
        # получить переданный массив из тела запроса
        allarray = api.payload['array']
        # возвратить новый созданный массив клиенту
        return {'len': str(len(allarray)), 'array': allarray}


minmax = api.model('minmax', {
                   'min': fields.String, 'max': fields.String}, required=True, description='two values')


@name_space1.route("/minmax")
class MinMaxClass(Resource):
    @name_space1.doc("")
    # маршаллинг данных в соответствии с моделью minmax
    @name_space1.marshal_with(minmax)
    def get(self):
        """Получение Максимума и Минимума массива"""
        global allarray
        return {'min': min(allarray), 'max': max(allarray)}

reqp.add_argument('len', type=int, required=False)
reqp.add_argument('minval', type=float, required=False)
reqp.add_argument('maxval', type=float, required=False)

@name_space1.route("/makerand")
class MakeArrayClass(Resource):
    @name_space1.doc("")
    # маршаллинг данных в соответствии с моделью minmax
    @name_space1.expect(reqp)
    @name_space1.marshal_with(list_)
    def get(self):
        """Возвращение массива случайных значений от min до max"""
        args = reqp.parse_args()
        array = [random()*(args['maxval']-args['minval'])+args['minval']
                 for i in range(args['len'])]
        return {'len': args['len'], 'array': array}


# api.add_namespace(name_space1)
