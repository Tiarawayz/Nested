x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print (x)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print (students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory ['soccer'][0] = 'Andres'
print (sports_directory['soccer'])

z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print (z)


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(list):
    for i in range(0,len(list)-0):
        output = ""
        for key,val in list[i].items():
            output += f' {key} - {val},'
            print (output)
iterateDictionary(students)

def iterateDictionary2(key_name, list):
    for i in range(0, len(list)):

        for key,val in list[i].items():
            if key ==key_name:
                print(val)
iterateDictionary2('first_name', students)
iterateDictionary2('last_name',students)

dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(place):
    for key,val in place.items():
        print (f'{len(val)} {key.upper()}')
        for i in range (0,len(val)):
            print (val[i])

print_info(dojo)