class Category:
    def __init__(self, description):
        self.description = description
        self.ledger = []
        self.balance = 0


    def deposit(self, amount, description=''):
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})
        
    def withdraw(self, amount, description):
        if self.balance - amount >= 0:
            self.ledger.append({'amount': -1 * amount, 'description':description})
            self.balance -= amount
            return True 
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, description):
        if Category.withdraw(self, amount, f'Transfer to {description}'):
            Category.deposit(self, amount, f'Trasnfer from {}')
        else:
            return False

    def check_funds(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False

    def __repr__()



def create_spend_chart(catgories):
    pass