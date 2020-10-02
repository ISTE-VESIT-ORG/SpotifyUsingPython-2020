class BankAcc:
	
	def __init__(self):
		self.balance = 10000

	def setBalance(self,value):
		self.balance = value

	def getBalance(self):
		return self.balance
		

obj = BankAcc()

obj.setBalance(0000)
print(obj.getBalance())

obj.setBalance(999)
print(obj.getBalance())

