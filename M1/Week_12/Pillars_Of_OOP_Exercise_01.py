class BancAccount():
    def __init__(self, balance):
        self.balance = balance


    def add_money(self):
        self.balance = self.balance + int(input('How much money do you want to add to your Bank Account?\n'))


    def withdraw_money(self):
        self.balance = self.balance - int(input('How much money do you want to withdraw?\n'))


class SavingAccount(BancAccount):
    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance


    def withdraw_money(self):
        new_balance = self.balance - int(input('How much money do you want to withdraw?\n'))
        if new_balance < self.min_balance:
            print('\nError, the balance is under the minimum balance or the amount to withdraw leaves the balance under the minimum balance.\n')
        else:
            self.balance = new_balance

saving_account = SavingAccount(500, 200)
print(f'Your current balance is: {saving_account.balance}')
saving_account.add_money()
saving_account.withdraw_money()
print(f'Your new balance is: {saving_account.balance}')