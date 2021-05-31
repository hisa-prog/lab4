
from flask_restplus import Resource, Namespace, fields
import json

from .models.ticket import Ticket


DB = {}

lottery_ns = Namespace('lottery', description='API для лотереи')

ticket = lottery_ns.model(
    "Ticket",
    {
        "fields": fields.List(fields.Integer, description='Значения полей на лотерейном билете', required=True),
        "price": fields.Float(description="Цена лотерейного билета", required=True),
    },
)


@lottery_ns.route("/<int:ticket_num>")
@lottery_ns.param('ticket_num', 'Номер лотерейного билета')
@lottery_ns.response(400, 'Нерпавильные данные')
@lottery_ns.response(404, 'Лотерейный билет не найден по номеру')
class TicketResource(Resource):
    @lottery_ns.expect(ticket)
    def post(self, ticket_num):
        """
        Метод для внесения лотирейного билета в базу
        """
        global DB
        json_data = lottery_ns.payload

        if ticket_num not in DB:
            ticket_fields = json_data['fields']
            ticket_price = json_data['price']
            if len(ticket_fields) != 3:
                return "Количество полей в билете должно быть равно 3", 400
            new_ticket = Ticket(ticket_num, ticket_fields, ticket_price)
            DB[ticket_num] = new_ticket
            return new_ticket.jsonify()
        else:
            return "Билет с этим номером уже есть в базе", 400

    def get(self, ticket_num):
        """
        Метод для получения информации о лотирейном билете
        """
        global DB
        if ticket_num in DB:
            return DB[ticket_num].jsonify()
        else:
            return "Лотерейный билет не найден", 404

    def patch(self, ticket_num):
        """
            Метод для изменения статуса билета (вызвается во время покупки билета в ларьке)
        """
        global DB
        if ticket_num in DB:
            DB[ticket_num].sell()
            return DB[ticket_num].jsonify()
        else:
            lottery_ns.abort(404)
