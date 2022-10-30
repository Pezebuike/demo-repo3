"""ist define a class """

#class
class Parrot:

    """then you define the class attribute
    by crating variable """ 
    #Class attribute 
    spacie = "bird"

    """in the init function you will store all 
    instance attirbute of the class 
    Example the name and the age of the parrot  """
    #instance class attribute
    def __init__ (self, name , age):
        """then call the self function becouse it's a key word  
        that must always be present in the init function"""
        self.name = name 
        self.age = age 

        """in every class there is the attribute and the beheviour
        this can be archived by creating function for it """

        #Instance Behaviour
    def dance(self):
        return "{} is dancing and i am {} years old ".format(self.name, self.age)
    def fly(self):
        return "{} is {} year old".format(self.name, self.age)  
    def song(self,song):
        return "{} is {}". format(self.name,song) 
     

"""after creating the class and its attribute, 
then we start talking about the object of the 
class which is the instance of a class """

# object ( instance of the class)
foo=Parrot("foo", 36)
gof=Parrot(name="gof",age = 10)

"""alternatively, we can still say the keyword style
foo=parrot(nmame ="foo", age = 36)"""

"""Accessing the instance attribute 
we use the dot oppaerator to do this"""

print("{} is {} years old".format(foo.name, foo.age))
print("{} is {} years old".format(gof.name, gof.age))

""" Lets accessing your class attribute"""

print("foo is {}".format(foo.spacie))
""" anpother mathod of accessing the class """
print("foo is {}".format(foo.__class__.spacie))

""" Access the intance behaivour """
print(foo.dance())
print(gof.dance())
print(foo.fly())
print(gof.fly())
print(gof.song("happy"))
print(foo.song("flying"))




        
