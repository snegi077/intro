


class saving_account :
	def __init__(self):
		self.balance=0
		print("Hello!!! Welcome to the ATM machine")

	def deposit(self):
		amount=float(input("Enter amount to be Deposited: "))
		self.balance += amount
		print("\n Amount Deposited:",amount)

	def withdraw(self):
		amount = float(input("Enter amount that your want to withdraw : "))
		if self.balance>=amount:
			self.balance-=amount
			print("\n You have  Withdrawn:", amount)
		else:
			print("\n Insufficient funds ")

	def display(self):
		print("\n  Balance=",self.balance)

s = saving_account()


s.deposit()
s.withdraw()
s.display()
