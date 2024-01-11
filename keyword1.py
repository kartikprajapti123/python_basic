x = 25
y = 20

z = x > y
print(z)  # True
x = 10
y = 20

# and to combine to conditions
# both need to be true to execute if block
if x > 5 and y < 25:
    print(x + 5)

# or condition
# at least 1 need to be true to execute if block
if x > 5 or y < 100:
    print(x + 5)

# not condition
# condition must be false
if not x:
    print(x + 5)
    
    
x = 10
y = 11 
z = 10
print(x is y) # it compare memory address of x and y 
print(x is z) 


x = 75
if x > 100:
    print('x is greater than 100')
elif x > 50:
    print('x is greater than 50 but less than 100')
else:
    print('x is less than 50')
    
    
    
    print('for loop to display first 5 numbers')
for i in range(5):
    print(i, end=' ')

print('while loop to display first 5 numbers')
n = 0
while n < 5:
    print(n, end=' ')
    n = n + 1