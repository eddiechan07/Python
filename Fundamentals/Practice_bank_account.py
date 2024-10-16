class BankAccount:
    # don't forget to add some default values for these parameters!
    bank_name = "National Bank"
    accounts =[]

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient Fund! Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    def display_account_info(self, account_name):
        print(f"Your Balance is {self.balance:.2f}, Interest-rate is {self.int_rate}")
        return self
    def yield_interest(self):
        if self.balance >0:
            self.balance += self.balance * self.int_rate
        return self
    @classmethod
    def all_accounts_info(cls):
        for account in cls.accounts:
            account.display_account_info()


Eddie_account = BankAccount(0.02, 0)
Allen_account = BankAccount(0.01, 0)

Eddie_account.deposit(100).deposit(200).deposit(300).withdraw(100).yield_interest().display_account_info()
Allen_account.deposit(300).deposit(200).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()
BankAccount.all_accounts_info()