my_list = list([2, 4, 6, 8, 10, 12])

# modify single item
my_list[0] = 20
print(my_list)
# Output [20, 4, 6, 8, 10, 12]

# modify range of items
# modify from 1st index to 4th
my_list[1:4] = [40, 60, 80]
print(my_list)
# Output [20, 40, 60, 80, 10, 12]

# modify from 3rd index to end
my_list[3:] = [80, 100, 120]
print(my_list)
# Output [20, 40, 60, 80, 100, 120]

my_list = list([2, 4, 6, 8, 10, 12])

# remove item present at index 2
my_list.pop(2)
print(my_list)
# Output [2, 4, 8, 10, 12]

# remove item without passing index number
my_list.pop()
print(my_list)
# Output [2, 4, 8, 10]

mylist = [3, 4, 5, 6, 1]
print(max(mylist)) #returns the maximum number in the list.
print(min(mylist)) #

mylist = [3, 4, 5, 6, 1]

print(sum(mylist)) 

#with all true values
samplelist1 = [1,1,True]
print("any() True values::",any(samplelist1))

#with one false
samplelist2 = [0,1,True,1]
print("any() One false value ::",any(samplelist2))


#with all false
samplelist3 = [0,0,False]
print("any() all false values ::",any(samplelist3))

#empty list
samplelist4 = []
print("any() Empty list ::",any(samplelist4))