# statement 1
print('Hello')

# statement 2
x = 20

# statement 3
print(x)

# two statements in a single
l = 10; b = 5

# statement 3
print('Area of rectangle:', l * b)

# Output Area of rectangle: 50

addition = 10 + 20 + \
           30 + 40 + \
           50 + 60 + 70
print(addition)


addition = (10 + 20 +
            30 + 40 +
            50 + 60 + 70)
print(addition)



# create a function
def fun1(arg):
    pass  # a function that does nothing (yet)


x = 10
y = 30
print(x, y)

# delete x and y
del x, y

# try to access it
# print(x, y)


# Define a function
# function acceptts two numbers and return their sum
def addition(num1, num2):
    return num1 + num2  # return the sum of two numbers

# result is the return value
result = addition(10, 20)
print(result)


# lets dicuss about break and continue in python 
for i in range(10):
    if i == 5:
        break
    print(i)
    
    
for i in range(10):
    if i == 8:
        continue 
    
    print(i)
    
print("hello2")
