class Category:
    def __init__(self, description):
        self.description = description
        self.ledger = []
        self.balance = 0


    def deposit(self, amount, description=''):
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})
        
    def withdraw(amount, description):
        if self.balance - amount >= 0:
            self.ledger.append({'amount': -1 * amount, 'description':description})
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount,  description):
        pass
