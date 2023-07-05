# # Update Values in Dictionaries and Lists
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# # 1 - 
# x[1][0]=15
# print(x)

# # 2 - 
# students[0]['last_name'] = 'Bryant'
# print(students)

# # 3 - 
# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory)

# # 4 - 
# z[0]['y'] = 30
# print(z)


# # Iterate Through a List of Dictionaries
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'},
#     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#     {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# def iterateDictionary(students):
#     for i in range(0, len(students)):
#         # print(students[i])
#         print(f"first_name: {students[i]['first_name']}, last_name: {students[i]['last_name']}")

# iterateDictionary(students)
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# # first_name - Michael, last_name - Jordan
# # first_name - John, last_name - Rosales
# # first_name - Mark, last_name - Guillen
# # first_name - KB, last_name - Tonel


# # Get Values From a List of Dictionaries
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'},
#     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#     {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterateDictionary2(first_name,students):
#         for i in students:
#             print(i['first_name'])
# iterateDictionary2('first_name',students)

# def iterateDictionary2(last_name,students):
#         for i in students:
#             print(i['last_name'])
# iterateDictionary2('last_name',students)


# Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    numLocations = len(dojo['locations'])
    numInstructors = len(dojo['instructors'])
    print(f"{numLocations} Locations")
    for i in dojo['locations']:
        print(i)
    print()
    print(f"{numInstructors} Instructors")
    for i in dojo['instructors']:
        print(i)

printInfo(dojo)