#create a basic class
class Book:
    #initializer function
    # 2 arguments, the self is the object itself, the convention name is self
    def __init__(self, title) -> None:
        self.title = title



b1 = Book("Brave new world")
b2 = Book("War and Peace")

print(b1.title)
print(b2.title)