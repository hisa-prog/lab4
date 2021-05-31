from flask_restplus import Namespace, Resource, fields
part_ns = Namespace('part', description='some information')

info = part_ns.model('part', {
    'id': fields.String(required=True, description='The identifier'),
    'name': fields.String(required=True, description='The name'),
})

INFO = [{'id': '1111', 'name': 'Alex'}]


@part_ns.route('/')
class InfoList(Resource):
    @part_ns.marshal_list_with(info)
    def get(self):
        '''List all / это описание появится в браузере на экране напротив get'''
        return INFO


@part_ns.route('/<id>')
@part_ns.param('id', 'The identifier')
@part_ns.response(404, 'id not found')
class InfoId(Resource):
    @part_ns.doc(params={'id': 'An ID'}) # описание id в документации по адресу 127.0.0.1
    @part_ns.marshal_with(info)
    def get(self, id):
        for idi in INFO:            
            if idi['id'] == id:                
                return idi
            else:            
                return {'id': id, 'name': 'your name'},
            part_ns.abort(404)
