students={
    'name':"kartik",
    'std':12,
    'subjects':
        ['hindi','english','maths','etc'],
    'gender':'male',
    'hobbies':['cricket','football','etc']
    
}

a=students['hobbies']
b=students['std']
print(a,b)

del students['name']

print(students)

students['behaviour']='pushes himself everytime'
print(students)

print(students.keys())

print(students.values())
print(students.get('hobbies'))

#dictionary with both 'true' keys
dict1 = {1:'True',1:'False'}

#dictionary with one false key
dict2 = {0:'True',1:'False'}

#empty dictionary
dict3= {}

#'0' is true actually
dict4 = {'0':False}

print('All True Keys::',all(dict1))
print('One False Key',all(dict2))
print('Empty Dictionary',all(dict3))
print('With 0 in single quotes',all(dict4))


dict = {1:'aaa',2:'bbb',3:'AAA'}
print('Maximum Key',max(dict)) # 3
print('Minimum Key',min(dict)) # 1

telephone_book = [1178, 4020, 5786]
persons = ['Jessa', 'Emma', 'Kelly']

telephone_Directory = {key: value for key, value in persons}
print(telephone_Directory)


