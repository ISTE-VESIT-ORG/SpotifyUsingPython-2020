
'''
List 

'''
xs = [3, 1, 2]   # Create a list
print(xs, xs[2])
print(xs[-1])     # Negative indices count from the end of the list; prints "2"

xs[2] = 'foo'    # Lists can contain elements of different types
print(xs)

xs.append('bar') # Add a new element to the end of the list
print(xs)  

x = xs.pop()     # Remove and return the last element of the list
print(x, xs)

'''
Tuple

'''
d = {(x, x + 1): x for x in range(10)}  # Create a dictionary with tuple keys
t = (5, 6)       # Create a tuple
print(type(t))
print(d[t])       
print(d[(1, 2)])

t[0] = 1 # 'tuple' object does not support item assignment

'''

Range 
syntax : -

range(start,end+1,step)

'''

print(range(1,11,1))
print(type(range(10)))