#create a basic class
class Book:
    #initializer function
    # 2 arguments, the self is the object itself, the convention name is self
    def __init__(self, title,author,pages,price) -> None:
        # properties
        self.title = title
        self.pages = pages
        self.authot = author
        self.price = price
        # this attribute can't be accessible out of class 
        self.__secret = "this is secrect attribute"

        # instance method
    def getPrice(self):
        if hasattr(self,"_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    
    def setDiscount(self,amount):
        #_ in front of attribute name to, this attribute uses internally 
        self._discount = amount


class Newspaper:
    def __init__(self, name) -> None:
        self.name = name



b1 = Book("Brave new world",'XXX',1000,230)
b2 = Book("War and Peace",'ZZZ',1000,260)

n1 = Newspaper("Stampa")
n2 = Newspaper ("Times")

print(type(b1)) # Book type
print(type(n1)) # Newspaper type 

print(type(b1) == type(n1))
print(type(b1) == type(b1))

# using instance
print(isinstance(b1,Book))
print(isinstance(n1,Newspaper))
print(isinstance(b1,Newspaper))

#print the price of books
#print(b2.getPrice())
#b2.setDiscount(0.25)
#print(b2.getPrice())