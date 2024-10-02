#List


l=[]
l= list()
l.append(1)
print(l)


#It can consist any datatype in a same list.
list= [1,2,4,5, 6, "Nitesh", "Kathmandu", 3.14, 0.71, 0.88]

#1
print(list[0])
print(list[-1])
print(list[0:6])


#2
list.append("Barcelona")
print(list)

list.append("K chha latest?")
print(list)


#3
list.insert(2,"Paris")
print(list) 

list.insert(3,"Dhulikhel")
print(list)

courses=["math","science"]
list.insert(0,courses)  #insert the entire courses list into the list's 0th index.
print(list)


#4
list.pop()  #removes "barcelona" from the last index.
print(list)

list.pop(3)
print(list)  #it removes the 3rd index which is "Paris".

print(list[0])
list.pop(0)
print(list)


#5
name=["James","Harry","Jonas","Jess"]  
list.extend(name) #it will by default add the name list into last index.
print(list)


#6
list.reverse()
print(list)


#7
num=[1,5,7,44,22,35, 1.2, 99, 88, 71.2]
num.sort() #method
print(num)

sorted_values= sorted(num) #function
print(sorted_values)


#8
min_val=min(num)
print(min_val)

max_val=max(num)
print(max_val)

sum_num=sum(num)
print(sum_num)


#9
num1=[1,2,22]
index_of_val=num1.index(22)
print(index_of_val)

index_another= num1.index(2)
print(index_another)



#10
cars=["Ferrari enzo", "Mercedez benz", "Lamborgini", "Porsche", "Supra"]
for index, car in enumerate(cars, start=1 ):
    print(index,car)
    
    
#11
cars=["Ferrari enzo", "Mercedez benz", "Lamborgini", "Porsche", "Supra"]
cars_str = "-".join(cars)  #joining each element of cars using '-'.
print(cars_str)


#12
new_cars_list=cars_str.split("-")
print(new_cars_list)

#13.
city=["A", "B", "C", "D"]
for index, cities in enumerate(city, start=0):
    print(index, cities)
    
#14.
list=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
for nums in list:
    if nums%2==0:
        even.append(nums)
    else:
        odd.append(nums)

print(even)
print(odd)
