# class - Property and Function
# Objects - 
# Assiuming we have the following attributes


Person1 = ['Michael Ezebuike ', 41, 4-7-1981]
Person2 = ['Francsica Opara', 39,  1-6-1983]
Person3 = ['Oliver michael ',  9, 1981-4-7]
Person4 = ['Chimamanda Adiala Michael',  1, 23-6-2021]

# Defining a python class
# use the 'Pass' commmand if you dont want to put anything in the class 

class PersonProfile:
    #properties
    name = 'Michael Ezebuike'
    age = 41
    DOB = 1981-4-7

    #fucntion 

    def sayname(name , age, DOB):
        print('{} was born in {}, he is {} years old'.format(name, age , DOB))

#OBJECT

person1 = PersonProfile()
print(person1.name )
print(person1.age )
print(person1.DOB )
print(person1.sayname(name= person1.name, age = person1.age, DOB= person1.DOB))




