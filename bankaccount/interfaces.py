from zope.interface import Interface, Attribute


class IBankAccount(Interface):
    balance = Attribute("balance")

    def deposit(amount):
        ...

    def withdraw(amount):
        ...
