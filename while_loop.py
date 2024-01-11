count = 1
# condition: Run loop till count is less than 3
while count < 3:
    print(count)
    count = count + 1
    
    
count = 1
# run loop till count is less than 5
while count < 5:
    print(count)
    count = count + 1
    
    
    
number = int(input('Enter any number between 100 and 500 '))
# number greater than 100 and less than 500
while number < 100 or number > 500:
    print('Incorrect number, Please enter correct number:')
    number = int(input('Enter a Number between 100 and 500 '))
else:
    print("Given Number is correct", number)



n = int(input('Please Enter Number '))
while n > 0:
    # check even and odd
    if n % 2 == 0:
        print(n, 'is a even number')
    else:
        print(n, 'is a odd number')
    # decrease number by 1 in each iteration
    n = n - 1
