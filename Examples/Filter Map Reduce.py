class Person:
    def _int_(self, name, age):
        self.name = name
        self.age = age
         
    def detail(self):
        print (self.name)
        print (self.age)
         
obj1 = Person("santos", 18)
obj1.detail()
comp2.config()