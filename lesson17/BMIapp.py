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
    def calculate_bmi(self):
        pass
    @abstractmethod
    def get_bmi_category(self):
        pass
    def print_info(self):
       return f"{self.name}, Age:{self.age}, weight: {self.weight}kg, Height:{self.height}m"
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
            return self.weight / (self.height ** 2) * 1.3

        def get_bmi_category(self):
            bmi = self.calculate_BMI()
            if bmi < 14:
                return "Underweight"
            elif 14 <= bmi < 18:
                return "Normal"
            elif 18 <= bmi < 24:
                return "Overweight"
            else:
                return "Obese"


class BMIApp:
    def __init__(self):
        self.people=[]
    def add_person(self,person):
        self.people.append(person)
    def collect_user_data(self):
        st.title("BMI calculator")
        name=st.text_input("Enter name:")
        age=st.number_input("Age:")
        weight=st.numbet_input("Weight in kg", min_value=0,max_value=0,value=25)
        height=st.number_input("height in meters", min_value=0.0, value=1.75)
        if st.button("Add Person"):
            if age>=18:
               person=Adult(name, age, weight,height )
            else: person

