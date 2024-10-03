person={"Name":"Nitesh", "Age":21}

print(f"My name is {person["Name"]} and my age is {person["Age"]}.")

print("My name is {0[Name]}, and my age is {1[Age]}".format(person,person)) 

#1.
class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
p1=person("Jack", 31)
print(f"Hi! this is {p1.name} and I am {p1.age} yrs old.")

#2.
person={"Name":"Samrajya", "Age":21}
print("my name is {Name} and my age is {Age}".format(**person))

#3.
pi=3.14159265
print("The value of pi is {:.3f}".format(pi)) #print upto 3rd decimal point.
# : help us to specify that we need some formatting over the value.
#like if we want to specify and modify something over the value we can do that by using : and specifying what we want.

print("The value of pi is {:.03}".format(pi))  #print only 3 numbers.

#4.
x=100000000
print("The value of x is {:,}".format(x))  #It helps to put comma the numbers.

#5.
import datetime
my_date= datetime.datetime(2024, 7, 9, 15, 46, 10)
print(my_date)

date_format= "{: %B %d, %Y}".format(my_date)  #we have specified that we want the date in month-date-and year format.
print(date_format)



movies={"A":"Inception", "B":"Intersteller"}
print("Movie is {A} and another movie is {B}".format(**movies))
print(f"Movie is {movies["A"]} and another movie is {movies["B"]}")



import datetime 
today_date= datetime.datetime.today()
print(today_date)

date_format= "{:%d %B, %Y}".format(today_date)
print(date_format)

x=2345678
print("The value of X is {:,}".format(x))


x=[1,2,3,4,5,6,7,8,9,0]
print( list(filter(lambda n: n%2!=0, x)))


class Maths():
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
        
    def __repr__(self):
        return f"The marks of {self.name} is {self.marks}"
        
n1=Maths("Nitesh", 91)
n2=Maths("Samrajya", 90)

n=[n1,n2]
print(n)

school={"Name":"Nitesh", "Age":22}
print("Name of the boy is {Name} and his age is {Age}".format(**school))