from abc import ABC,abstractmethod

class Person(ABC):
    def __init__(self,name,age,weight,height):
        self.name=name
        self.age=age
        self._weight=weight
        self._height=height

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self,value):
        if value<0:
            raise ValueError("weight cannot be negative")
        self._weight=value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
       self._height=value

    @abstractmethod
    def calculate_BMI(self):
        pass
    @abstractmethod
    def get_bmi_category(self):
        pass
    def print_info(self):
        print(f"{self.name}, Age:{self.age}, weight: {self.weight}kg, Height:{self.height}m")
        print(f"BMI: {self.calculate_BMI():.2f}, Category: {self.get_bmi_category()}")

class Adult(Person):
    def calculate_BMI(self):
        return self.weight/(self.height**2)
    def get_bmi_category(self):
        bmi=self.calculate_BMI()
        if bmi<18.5:
            return "Underweight"
        elif 18.5<=bmi<24.9:
            return "Normal"
        elif 24.9<= bmi<29.9:
            return "Overweight"
        else:
            return "Obese"

class Child(Person):
    def calculate_BMI(self):
        return self.weight / (self.height ** 2)*1.3
    def get_bmi_category(self):
        bmi=self.calculate_BMI()
        if bmi<14:
            return "Underweight"
        elif 14<=bmi<18:
            return "Normal"
        elif 18<= bmi<24:
            return "Overweight"
        else:
            return "Obese"
class BMIApp:
    def __init__(self):
        self.people=[]
    def add_person(self,person):
        self.person.append(person)
    def collect_user_data(self):
        name=int(input(" Enter name "))
        age=int(input(" Enter age "))
        weight=float(input(" Enter Weight in kg "))
        height=float(input(" Enter Height in m "))
        if age>18:
            person=Adult(name,age,weight,height)
        else:
            person=Child(name,age,weight,height)
        self.add_person(person)
    def print_result(self):
        for person in self.people:
            person.print_info()
    def run(self):
        while True:
            self.collect_user_data()
            cont=input("Do you want to add a person").strip().lower()

            if cont!="Y":
                break
        self.print_result()

app=BMIApp()
app.run()


import numpy as np

arr_2d=np.array([1,2.3,54],[8,3,4,5,])

print(arr_2d)











