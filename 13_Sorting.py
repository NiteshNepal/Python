"""list=[2,3,1,-1,5,6,7,3,2,0]

sort= sorted(list, reverse=True) #sorted function requies a new variable. 
#reverse helps to sort the value in descending order.
print(sort)

list.sort() #sorted method sorts the original list.
print(list)


#Tuple
#we cannot sort the tuple using sort() method, so we need to sort them using sorted() function.
tup=(4,5,1,3,2,4,8,9)
sorted_tup= sorted(tup)
print(sorted_tup)


#Dictionary
dict_data= {"Name":"Nitesh", "Age": 21, "Studies":"Data Science"}
sorted_dict=sorted(dict_data, reverse=True)
print(sorted_dict)"""

class Employees():
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        
    def __repr__(self):
        return f"{self.name},{self.age},${self.salary}"

e1=Employees("Nitesh", 21, 1000000000)
e2=Employees("Samrajya", 22, 20000000)
e3=Employees("Brad", 32, 3000000000)

employees=[e1,e2,e3]

sorted_employees=sorted(employees, key=lambda e: e.age)  #sorting the list based on name.
print(sorted_employees)

#we can also sort the value based on the builtins called as attrgetter.
from operator import attrgetter
s_employees= sorted(employees, key=attrgetter("age"))
print(s_employees)



class Store():
    def __init__(self, name, price):
        self.name=name
        self.price=price
        
    def __repr__(self):
        return f"{self.name}, {self.price}"
    
item1= Store("Waiwai", 10)
item2= Store("Biscuit", 20)

item=[item1, item2]

print(item)

sorted_items= sorted(item, key=lambda n: n.price)
print(sorted_items)

sortedd_items= sorted(item, key=lambda n: n.name)
print(sortedd_items)