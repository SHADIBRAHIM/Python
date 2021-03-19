class bank:
    def __init__(self):
        self.bal=0
        self.acno=int(input("Enter account no: "))
        self.name=input("Enter account holder name: ")
        self.actype=input("Enter type of account: ")

    def display(self):
        print("Name :",self.name)
        print("Account no: ",self.acno)
        print("Type of account: ",self.actype)

    def deposit(self):
        amount=int(input("enter the amount to be deposited: "))
        self.bal+=amount
        print("Balance after deposit: ",self.bal)

    def withdraw(self):
        amount=int(input("Enter the amount to be withdrawn: "))
        if(amount>self.bal):
            print("Cannot be withdrawn.Amount is higher than available balance")
        else:
            self.bal-=amount
            print("Balance after withdrawal: ",self.bal)

account=bank()
account.display()
account.deposit()
account.withdraw()