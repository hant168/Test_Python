class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self._account_number = account_number
        self._owner = owner
        self.balance = balance

    @property
    def owner(self):
        return self._owner

    @property
    def account_number(self):
        return self._account_number

    # @property
    # def account_name(self):
    #     return self._account_name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            raise ValueError("Số dư phải lớn hơn 0")

    def display(self):
        print(self.account_number, self.owner, self.balance, "₫")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError(
                "Số tiền phải lớn hơn 0 và không được vượt quá số dư hiện tại")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Số tiền phải lớn hơn 0")


# my_account = BankAccount(1, "Ha", 1000000000)
# my_account.deposit(1_000_000_000_000_000_000)
# my_account.display()

# my_account.withdraw(100_000_000)  # quá nhỏ bé 😊
# my_account.display()


class Customer():
    def __init__(self, name, date_of_birth, email, phone):
        self.name = name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone = phone

    def get_info(self):
        print(self.name, self.date_of_birth, self.email, self.phone)


class SavingAccount(BankAccount):
    monthly_interest_rate = 0.005

    def __init__(self, account_number, account_name, balance=0):
        super().__init__(account_number, account_name, balance)

    def calculate_interest(self):

        return self.balance * self.monthly_interest_rate

    def display(self):
        print("Acc Number:",self.account_number, "Balance:",
              self.balance, "Interest Rate:",self.monthly_interest_rate)

        if self.owner is Customer:
            self.owner.get_info()


savingacount = SavingAccount(192449001, "Ha", 2000000)
savingacount.display()
# print(savingacount.calculate_interest())


customer = Customer("Ha", "1-2-1999", "hant@gmail.com", "092123333")
# customer.get_info()


# Pass customer vào luôn owner của SavingAccount 
savingacount = SavingAccount(1111, customer, 123)
savingacount.display()
