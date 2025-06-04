class Bank:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def show_details(self):
        return f"Account Holder: {self.account_holder}, Balance: ₹{self.balance}"

class SavingAccount(Bank):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def saving_info(self):
        return f"Saving Account | Interest Rate: {self.interest_rate}%"

class CurrentAccount(Bank):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def current_info(self):
        return f"Current Account | Overdraft Limit: ₹{self.overdraft_limit}"

class FixedDeposit(Bank):
    def __init__(self, account_holder, balance, duration_years):
        super().__init__(account_holder, balance)
        self.duration_years = duration_years

    def fd_info(self):
        return f"Fixed Deposit | Duration: {self.duration_years} years"

# Create objects
saving = SavingAccount("Radha", 20000, 4.5)
current = CurrentAccount("Krishna", 50000, 10000)
fd = FixedDeposit("Balram", 100000, 5)

# Print info
print(saving.show_details())
print(saving.saving_info())

print(current.show_details())
print(current.current_info())

print(fd.show_details())
print(fd.fd_info())
