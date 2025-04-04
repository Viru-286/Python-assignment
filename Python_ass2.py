#Checking if a number is even or odd

a = int(input('Enter a number: '))

if (a % 2 == 0):
  print(a,'is Even number:')
else:
  print(a,'is odd number:')
  
  
#Sum of integers from 1 to 50 using loop
#Using for loop:
sum = 0
for x in range(1,51):
  sum += x
  x += 1

print(sum) 

#Using while loop:
Add = 0
a = 1
while(a<=50):
  Add += a
  a += 1

print(Add)