def multiplication(n):
    for i in range(1,11):
        print(i*n)
        
multiplication(7)


def recursive(n):
    if n==0 :
        return 1
    else:
        return n*recursive(n-1)
        
print(recursive(5))

def factorial(no):
    if no == 0:
        return 1
    else:
        return no * factorial(no - 1)

print("factorial of a number is:", factorial(8))


# lambda function in python 
a=lambda x,y:print(x,y) 
a(10,20)


def func(a):
    
       return a*a
   
    
a=[1,2,3,4]
b=list(filter(lambda x:x>=2,a))
b=list(map(func,a))
print(b)



# Global variable
x = 5

# defining 1st function
def function1():
    print("Value in 1st function :", x)

# defining 2nd function
def function2():
    # Modify global variable using global keyword
    global x #this is used to show the global in python 
    x = 555
    print("Value in 2nd function :", x)

# defining 3rd function
def function3():
    print("Value in 3rd function :", x)

function1()
function2()
function3()