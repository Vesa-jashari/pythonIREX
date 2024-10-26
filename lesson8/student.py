class Student:
    def __init__(self , name, age, course, notaMesatare ):
        self.name=name
        self.age=age
        self.course=course
        self.notaMesatare=notaMesatare #variable private


    def pershendetje(self):
        print(f'Hello , Une jam {self.name} dhe mesoj {self.course}')

    def _tregonnota(self):
        print("This is a protected Method")


Alma=Student("Alma",27,"python", 5.0)
Alma.pershendetje()