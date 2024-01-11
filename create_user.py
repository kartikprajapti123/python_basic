input_string = input('Enter elements of a list separated by space \n')
user_list = input_string.split()
print('string list: ', user_list)

# # # convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])

print('User list: ', user_list)
# Calculating the sum of list elements
print("Sum = ", sum(user_list))


number_list = []
n = int(input("Enter the list size "))

print("\n")
for i in range(0, n):
    print("Enter number at index", i, )
    item = int(input())
    number_list.append(item)
print("User list is ", number_list)


a=[i for i in range(1,10) ]
print(a)

