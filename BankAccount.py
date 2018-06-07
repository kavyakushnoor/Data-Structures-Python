__author__ = 'kavya'

class BankAccount:
    '''
    Stores information about a bank account including the first and last name of the account holder,
    and the account balance.
    '''

    def __init__(self, first, last, bal):
        '''
        The constructor for a bank account.
        :param first: The customer's first name.
        :param last: The customer's last name.
        :param bal: The balance of the account.
        :return: Nothing
        '''
        self.firstName = first
        self.lastName = last
        self.balance = bal

    def deposit(self, amt):
        '''
        Adds an amount to the account's balance.
        :param amt: The amount to add to the account.
        :return: Nothing.
        '''
        self.balance += amt

    def withdraw(self, amt):
        '''
        Deducts an amount from the account's balance.
        :param amt: The amount to deduct.
        :return: Nothing.
        '''
        self.balance -= amt

    def __str__(self):
        '''
        A pretty string to print for the BankAccount.  Should look like "Jones, Mary    $300"
        :return: The string for printing.
        '''
        return self.lastName + ", " + self.firstName + "\t$" + str(self.balance)

    def calculateInterest(self):
        '''
        Calculate the interest earned on the bank account assuming the interest rate is 1.5%
        :return: The calculated interest.
        '''
        return 0.015*self.balance




