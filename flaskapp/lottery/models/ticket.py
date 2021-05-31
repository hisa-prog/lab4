

class Ticket:
    def __init__(self, number, fields, price):
        self.number = number
        self.fields = fields
        self.price = price
        self.is_bought = False

    def sell(self):
        self.is_bought = True

    def is_lucky(self):
        unique_fields = set(self.fields)
        return len(unique_fields) == 1

    def jsonify(self):
        return {
            'ticket_num': self.number,
            'fields': self.fields,
            'price': self.price,
            'is_lucky': self.is_lucky(),
            'is_bought': self.is_bought
        }
