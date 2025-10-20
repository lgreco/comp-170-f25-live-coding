class Person:

    def __init__(self, first_name:str):
        # Special methods are recognized by the double 
        # underscores at the front and end of their 
        # name. That's why they are often called
        # dunder methods (Double UNDERscores)
        self.__first_name = first_name
        self.last_name = None
        self.bday_month = -1
        self.bday_day = -1
        self.phone_number = -1
        self.email = None
    
    def get_name(self):
        return f"My name is: {self.__first_name}"


## test code
p1 = Person("Leo")
print(p1.get_name())
print(p1._Person__first_name)