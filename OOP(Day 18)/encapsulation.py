# Encapsulation: wrapping data and methods together and hidding from outside access

'''
It is achived via acess control
public: variable
protected: _variable
private: __variable
'''

class Bank:
    def __init__(self):
        self.__balance = 5000

    def deposite(self, amount):
        self.__balance += amount
        print(f"Deposited: {self.__balance}")

    def show_balance(self):
        print(f"Availaible Balance: {self.__balance}")

acc = Bank()
acc.deposite(500)
acc.show_balance()
