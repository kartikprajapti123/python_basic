a=("hello",'kartik',12,12,"kartik","gautam")

print(set(a))


number_list = [20, 30, 20, 30, 50, 30]
# create a set from a list
sample_set = set(number_list)

print(sample_set)
# Output {50, 20, 3


sample_set = {'Mark', 'Jessa', [35, 78, 92]}
print(sample_set)

for book in sample_set:
    print(book)
    
    
book_set = {'Harry Potter', 'Angels and Demons'}
book_set.add('The God of Small Things')


color_set = {'red', 'orange', 'yellow', 'white', 'black'}

# remove single item
color_set.remove('yellow')
print(color_set)
# Output {'red', 'orange', 'white', 'black'}

# remove single item from a set without raising an error
color_set.discard('white')
print(color_set)
# Output {'orange', 'black', 'red'}

# remove any random item from a set
deleted_item = color_set.pop()
print(deleted_item)

# remove all items
color_set.clear()
print(color_set)
# output set()

# delete a set
del color_set


color_set = {'red', 'orange', 'white', 'black'}

# remove single item using discard()
color_set.discard('yellow')
print(color_set)
# Output {'red', 'black', 'white', 'orange'}

# remove single item using remove()
color_set.remove('yellow')
print(color_set)
# Output KeyError: 'yellow'