# class Animal():
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age 


#     def make_sound(self):
#         pass

#     def display_info(self):
#         pass

# class Lion(Animal):
#     def __init__(self, name, age):
#         super().__init__(name, age)

#     def make_sound (self):
#         print(f'{self.name} звучит ррр')

#     def display_info(self):
#         print(f"Животное:{self.name} \nВозраст:{self.age}")

# # lion = Lion("Лев", "12")
# # lion.make_sound()
# # lion.display_info()

# class Elephant(Animal):
#     def __init__(self, name, age):
#         super().__init__(name, age)

#     def make_sound (self):
#         print(f"{self.name} звучит ууу")

#     def display_info(self):
#         print(f"Животное:{self.name} \nВозраст:{self.age}")


# def introduce_animal(animal):
#         animal.make_sound()
#         animal.display_info()


# elephant = Elephant("Слон", "19") 
# lion = Lion("Лев", "12")

# introduce_animal(elephant)
# introduce_animal(lion)


# elephant = Elephant("Слон", "19") 
# elephant.make_sound()
# elephant.display_info()


class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return 0  
    

    def display_info(self):
        print(f"Сотрудник: {self.name}, Базовая ставка: {self.base_salary}")


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        fixed_coefficient = 1.2
        return self.base_salary * fixed_coefficient


class PartTimeEmployee(Employee):
    def __init__(self, name, base_salary, hours_worked):
        super().__init__(name, base_salary)
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.base_salary * 0.5 * self.hours_worked


def process_salary(employee):
    employee.display_info()
    salary = employee.calculate_salary()
    print(f"Зарплата: {salary}\n")


full_time_employee = FullTimeEmployee("Нуразиз", 1000001)
# part_time_employee = PartTimeEmployee("Аслан", 100, 300)

process_salary(full_time_employee)
# process_salary(part_time_employee)
