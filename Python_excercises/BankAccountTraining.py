class BankAccount:
    def __init__(self, start_balance: int = 0) -> None:
        self.account_balance = start_balance

    def deposit(self, money: int) -> None:
        self.account_balance += money

    def withdraw(self, money: int)-> None:
        if self.account_balance >= money:
            self.account_balance -= money
        else:
            print("Cannot withdraw money. Too small balance.")

    def withdraw2(self, money: int)-> None:
        if money <= self.account_balance:
            self.account_balance -= money
        else:
            raise ArithmeticError("Cannot have negative balance")

    def __str__(self) -> str:
        return str(self.account_balance)

account1 = BankAccount(5)
account1.deposit(5)
account1.withdraw2(12)
print(account1)