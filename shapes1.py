class shap:
    def __init__(self,name,color):
        self.name = name 
        self.color = color

    def area(self,length,breath):
        result = length*breath
        return result
    # def area(self, r):
    #     p = 3,147
    #     result =  p*r**2
    #     return result
square = shap('square', 'blue')
rect = shap('rectangle','green')

length =int(input('Enter the length '))
breath = int(input('Enter the breath '))

# circle = shap('circle','white')
# circle = shap('circle ','blue')

print("a {} {}".format(square.color, square.name))
#print("The area of the {} is {} ".format(square.name,square.area(7,5)))

print("The area of the {} is {} ".format(square.name,square.area(length,breath)))

