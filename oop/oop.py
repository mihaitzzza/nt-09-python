# x = 7
# x = 7.5
# x = 7.5 + 6j
# x = 'abc'
# x = lambda: 2
# print(type(x), x.__class__, type(type(x)))

# class Person:
#     def __init__(self, first_name, last_name):
#         self._first_name = first_name
#         self._last_name = last_name
#
#     @property
#     def first_name(self):
#         return self._first_name
#
#     @first_name.setter
#     def first_name(self, value):
#         is_admin = False
#         if is_admin:
#             self._first_name = value
#         else:
#             raise TypeError("You don't have access to this operation")
#
#     def introduce_yourself(self):
#         print(f'My name is {self._first_name} {self._last_name}')
#
#     def __str__(self):
#         return f'{self._first_name} {self._last_name}'
#
#
# # print(dir(MyFirstClass))
#
# student_1 = Person('Ion', 'Popescu')
# print(student_1.first_name)
# student_1.first_name = 'Grigore'
# print(student_1.first_name)
# # student_1.introduce_yourself()
# # # print('student_1.first_name', student_1.first_name)
# # student_1.first_name = '2222222222222222222'
# # student_1.introduce_yourself()
# # print('student_1', student_1)  # this calls the magic method __str__
#
# # student_2 = Person('Gigel', 'Frone')
# # print('student_2', student_2)  # this calls the magic method __str__


# class MyClass:
#     value = 20
#
#
# my_object_1 = MyClass()
# my_object_1.value = 70
#
# my_object_2 = MyClass()
#
#
# print(MyClass.value)
# print(my_object_1.value)
# print(my_object_2.value)


from abc import abstractmethod, ABC


class Animal:
    @staticmethod
    @abstractmethod
    def eat():
        pass

    @staticmethod
    @abstractmethod
    def talk():
        pass

    def my_function(self):
        print('[Animal] my_function')


class Elephant(Animal):
    @staticmethod
    def talk():
        print('Ugly sounds.')

    @staticmethod
    def eat():
        print('Eat bananas')

    def my_function(self):
        super().my_function()
        print('[Elephant] my_function')


class Person(Animal, ABC):
    @staticmethod
    def eat():
        print('Get some healthy food.')

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    def introduce_yourself(self):
        print(f'My name is {self._first_name} {self._last_name}')

    def my_function(self):
        print('[Person] my_function')

    def __str__(self):
        return f'{self._first_name} {self._last_name}'


class Male(Person):
    gender = 'M'
    has_long_hair = False

    @staticmethod
    def what_are_your():
        print('I am a male.')

    @staticmethod
    def talk():
        print('Hai la bere!')

    def my_function(self):
        # super().my_function()
        super(Person, self).my_function()
        print('[Male] my_function')


class Female(Person):
    gender = 'F'
    has_long_hair = True

    def __init__(self, first_name, last_name, color):
        super().__init__(first_name, last_name)
        self.color = color

    @staticmethod
    def what_are_your():
        print('I am a female.')

    @staticmethod
    def talk():
        print('Hai la gin!')

    def my_function(self):
        print('[Female] my_function')


# male = Male('Ion', 'Popescu')
# print('gender', male.gender)
# male.what_are_your()
# male.talk()
# male.introduce_yourself()
# print('\n')
# female = Female('Dana', 'Grigore')
# print('gender', female.gender)
# female.what_are_your()
# female.talk()
# female.introduce_yourself()
#
# print(female.eat())


# x = Elephant()
# x.my_function()

# male = Male(first_name='Ion', last_name='Popescu')
# male.my_function()

female = Female(first_name='Dana', last_name='Grigore', color='red')
print(female)
