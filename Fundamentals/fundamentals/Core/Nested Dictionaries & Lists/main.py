#Update Values in Dictionaries and Lists#
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30

#Iterate Through a List of Dictionaries#
def iterateDictionary(some_list):
    for d in some_list:
        output = ""
        for key, value in d.items():
            output += f"{key} - {value}, "
        print(output[:-2])  

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary(students)

#Get Values From a List of Dictionaries#
def iterateDictionary2(key_name, some_list):
    for d in some_list:
        print(d[key_name])

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
iterateDictionary2('first_name', students)

iterateDictionary2('last_name', students)

#Iterate Through a Dictionary with List Values#
def printInfo(some_dict):
    for key, value_list in some_dict.items():
        print("-" * 10)
        print(f"{len(value_list)} {key.upper()}")
        for value in value_list:
            print(value)
                 
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)