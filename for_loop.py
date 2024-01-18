sum = 0
for i in range(2, 22, 2):
    sum = sum + i
print(sum)
# output 110

numbers = [1, 2, 3, 4, 5]
# iterate over each element in list num
for i in numbers:
    # ** exponent operator
    square = i ** 2
    print("Square of:", i, "is:", square)
    
    
numbers = [10, 20, 30, 40, 50]

# definite iteration
# run loop 5 times because list contains 5 items
sum = 0
for i in numbers:
    sum = sum + i
list_size = len(numbers)
average = sum / list_size
print(average)

name = "mariya mennen"
count = 0
for char in name:
    if char != 'm':
        continue
    else:
        count = count + 1

print('Total number of m is:', count)


for i in range(1, 6):
    print(i)
else:
    print("Done")
    
count = 0
print("hello")
for i in range(1, 6):
    count = count + 1
    if count > 2:
        break
    else:
        print(i)
else:
    print("Done")
    
a="kartik1233"
list1 = [10, 20, 30, 40]
for num in reversed(a):
    print(num)