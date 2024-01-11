# arithmetic operator in python 
a=10
b=20
c=a+b
print(c)
c=a-b
print(c)
c=a/b
print(c)
c=a//b
print(c)
c =a**b
print(c)
c=a*b
print(c)

# relational operator in python 

x = 10
y = 5
z = 2

# > Greater than
print(x > y)  # True
print(x > y > z)  # True

# < Less than
print(x < y)  # False
print(y < x)  # True

# Equal to 
print(x == y)  # False 
print(x == 10)  # True 

# != Not Equal to 
print(x != y)  # True 
print(10 != x)  # False 

# >= Greater than equal to
print(x >= y)  # True
print(10 >= x)  # True

# <= Less than equal to
print(x <= y)  # False
print(10 <= x)  # True



a = 4
b = 2

a += b
print(a)  # 6

a = 4
a -= 2
print(a)  # 2

a = 4
a *= 2
print(a)  # 8

a = 4
a /= 2
print(a)  # 2.0

a = 4
a **= 2
print(a)  # 16

a = 5
a %= 2
print(a)  # 1

a = 4
a //= 2

print(a)  # 2


# logical operator and
a = 2
b = 4

# Logical and
if a > 0 and b > 0:
    # both conditions are true
    print(a * b)
else: 
    print("Do nothing")
    
    
    
# logical operator and
a = 2
b = 4

# Logical and
if a > 0 or b > 0:
    # both conditions are true
    print(a * b)
else:
    print("Do nothing")
    
    
a = True

# Logical operator not
if not a:
    # a is True so expression is False
    print(a) 
else:
    print("Do nothing")
    
    
    
    