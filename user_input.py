# program to calculate addition of two input integer numbers

# convert inout into int
first_number = int(input("Enter first number "))
second_number = int(input("Enter second number "))

print("\n")
print("First Number:", first_number)
print("Second Number:", second_number)
sum1 = first_number + second_number
print("Addition of two number is: ", sum1)


marks = float(input("Enter marks "))
print("\n")
print("Student marks is: ", marks)
print("type is:", type(marks))


# list to store multi line input
# press enter two times to exit
data = []
print("Tell me about yourself")
while True:
    line = input()
    if line:
        data.append(line)
    else:
        break
finalText = '\n'.join(data)
print("\n")
print("Final text input")
print(finalText)


# Python 2 code
# raw_input() function
name = input("Enter your name ")
print ("Student Name is: ", name)
print (type(name))

age = input("Enter your age ")
print ("Student age is: ", age)
print (type(age))