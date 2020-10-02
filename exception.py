
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


# print("Hello exceptions")

# try : 
# 	x = [1,2,3,4,5]
# 	print(x[9])
# except Exception as ex : 
# 	print("It seems you are trying to access index which is not in the list")

# print("Hello after exception")

# try : 
# 	x = 5/0
# except Exception as ex : 
# 	print(ex.__class__.__name__)