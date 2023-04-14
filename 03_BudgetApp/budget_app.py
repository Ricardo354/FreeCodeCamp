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
            Category.deposit(self, amount, f'Trasnfer from {description}')
        else:
            return False

    def check_funds(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False
         
    def __repr__(self):
        header = self.description.center(30,'*') + '\n'
        thingie = ''
        for i in self.ledger:
            desc = "{:<23}".format(i['description'])
            price = "{:>7.2f}".format(i['amount'])
            thingie += '{}{}\n'.format(desc[:23], price[:7])
                
        return header + thingie

p1 = Category('Food')
Category.deposit(p1,25,'initial deposit')
Category.deposit(p1,50,'final deposit')
Category.withdraw(p1,15.89,'restaurant and more food')
print(Category.__repr__(p1))

            

def create_spend_chart(catgories):
    pass