def myFun(*args): 
	print(len(args),type(args),args[0])
	for arg in args:
		print(arg)
myFun('Hello', 'Welcome', 'to', 'python workshop') 


def myFun1(**kwargs): 
	print(len(kwargs),type(kwargs),kwargs.keys())
	for i in kwargs:
		print(kwargs[i])
myFun(name ="VESIT",city="Mumbai") 

