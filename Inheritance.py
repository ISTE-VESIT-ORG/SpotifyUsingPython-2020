class A: 
	def __init__(self):
		print("INIT A")
	def feature1(self):
		print("Feature 1 in A working")
	def feature2(self):
		print("Feature 2 working")

class B(A) : 
	# def __init__(self):
	# 	super().__init__() 
	# 	print("INIT B")
	# def feature1(self):
	# 	print("Feature 1 in B working")
	def feature2(self):
		print("Feature 2 working")
		
# class C(A,B):
# 	def __init__(self):
# 		super(C,self).__init__()
# 		print("INTI C")
# 	def feature5(self):
# 		super().feature1()

# c = C()
# c.feature5()
