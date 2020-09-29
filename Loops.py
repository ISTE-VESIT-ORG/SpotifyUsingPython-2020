'''
Normal
For loop 

'''
for i in range(10):
	print(i)

animals = ['cat', 'dog', 'monkey']

for i in range(len(animals)):
	print(animals[i])

for animal in animals:
    print(animal)

'''
while loop

'''

count = 0
while (count < 5):      
    count += count+1 
    print("Hello this is while loop")  
  
print() 
  
# checks if list still 
# contains any element  

a = [1, 2, 3, 4] 
while a: 
    print(a.pop())

