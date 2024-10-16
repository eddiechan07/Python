class BankAccount:
    bank_name = "National Bank"
    accounts =[]

    def __init__(self, int_rate, balance):   #create BankAccount instance
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):      #create deposit method
        self.balance += amount
        return self
    def withdraw(self, amount):     #create withdraw method
        if amount > self.balance:
            print(f"Insufficient Fund! Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    def display_account_info(self, account_name):       #create display account info method based on account name
        print(f"Your {account_name} Account balance is {self.balance:.2f}, Interest-rate is {self.int_rate}")
        return self
    def yield_interest(self):       #create interest rate calculate method
        if self.balance >0:
            self.balance += self.balance * self.int_rate
        return self
    @classmethod
    def all_accounts_info(cls):
        for account in cls.accounts:
            account.display_account_info()
            

class User:
    def __init__(self, first_name, last_name, email, age):      #create User instance
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.accounts = {}
    def add_accounts(self, account_name, int_rate, balance):    #add user account (relate with BankAccount instance)
        self.accounts[account_name] = BankAccount(int_rate, balance)
        print(f"{self.first_name} {self.last_name} : Your {account_name} Account has been created")
        return self
    def make_deposit(self, account_name, amount):       #create User make deposit methof (relate with BankAccount deposite method)
        if account_name in self.accounts:
            self.accounts[account_name].deposit(amount)
        elsed
            print(f"{account_name} Account not found")
        return self
    def make_withdraw(self, account_name, amount):      #create User make withdraw method (relate with BankAccount withdraw method)
        if account_name in self.accounts:
            self.accounts[account_name].withdraw(amount)
        else:
            print(f"{account_name} Account not found")
        return self
    def display_account_info(self, account_name):       #create User display account info method (relate with BankAccount display account info method)
        if account_name in self.accounts:
            self.accounts[account_name].display_account_info(account_name)
        else:
            print(f"{account_name} Account not found")
        return self
    def transfer_money(self, account_name, amount, other_user):     #create User transfer money method (relate with BankAccount deposite/withdraw method)
        self.accounts[account_name].withdraw(amount)
        other_user.accounts[account_name].deposit(amount)
        return self

user1 = User("John", "Doe", "john.doe@example.com", 30)     #create User1 instance
user2 = User("Mike", "Lee", "mike.lee@example.com", 20)     #create User2 instance


user1.add_accounts("Checking", 0.02, 1000)      #add User1 Checking account with interest of 0,02 and balance of 1000
user1.add_accounts("Saving", 0.05, 500)         #add User1 Saving account with interest of 0,05 and balance of 500
user2.add_accounts("Checking", 0.02, 100)       #add User2 Checking account with interest of 0,02 and balance of 100
user2.add_accounts("Saving", 0.05, 100)         #add User2 Saving account with interest of 0,05 and balance of 100


user1.make_deposit("Checking", 200).make_withdraw("Saving", 200).display_account_info("Checking")     
user1.make_deposit("Saving", 100).make_withdraw("Checking", 200).display_account_info("Saving")

user1.transfer_money("Checking", 700, user2)     #transfer money of $700 from User1 Checking account to User2 Checking account
user2.display_account_info("Checking")           #dispaly User2 Checking account info