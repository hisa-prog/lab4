from flask_restplus import fields, Resource, reqparse, Namespace
from random import random


allarray = ['1']


list_np = Namespace('list', description='list APIs')


list_ = list_np.model('list',
                  {
                      'len': fields.String(required=True, description='Size of array'),
                      'array': fields.List(fields.String, required=True, description='Some array'),
                  })


@list_np.route("/")
class ListClass(Resource):
    @list_np.doc("")
    @list_np.marshal_with(list_)
    def get(self):
        """"Получение всего хранимого массива"""
        return {'len': str(len(allarray)), 'array': allarray}

    @list_np.doc("")
    @list_np.expect(list_)
    @list_np.marshal_with(list_)
    def post(self):
        """Создание массива/наше описание функции пост"""
        global allarray
        # получить переданный массив из тела запроса
        allarray = list_np.payload['array']
        # возвратить новый созданный массив клиенту
        return {'len': str(len(allarray)), 'array': allarray}


minmax = list_np.model('minmax', {
                   'min': fields.String, 'max': fields.String}, required=True, description='two values')


@list_np.route("/minmax")
class MinMaxClass(Resource):
    @list_np.doc("")
    # маршаллинг данных в соответствии с моделью minmax
    @list_np.marshal_with(minmax)
    def get(self):
        """Получение Максимума и Минимума массива"""
        global allarray
        return {'min': min(allarray), 'max': max(allarray)}


reqp = reqparse.RequestParser()
reqp.add_argument('len', type=int, required=False, default=10)
reqp.add_argument('minval', type=float, required=False, default=1)
reqp.add_argument('maxval', type=float, required=False, default=10)

@list_np.route("/makerand")
class MakeArrayClass(Resource):

    @list_np.doc("")
    # маршаллинг данных в соответствии с моделью minmax
    @list_np.expect(reqp)
    @list_np.marshal_with(list_)
    def get(self):
        """Возвращение массива случайных значений от min до max"""
        args = reqp.parse_args()
        array = [random()*(args['maxval']-args['minval'])+args['minval']
                 for i in range(args['len'])]
        return {'len': args['len'], 'array': array}
