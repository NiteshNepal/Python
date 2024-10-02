#sets doesn't have duplicate values.

s=set() #we must call set like this.     
s={} #It is not a set, but it is a empty dictionary.

num={1,2,3,4,5,6,6,6,7,7}
print(num)  #it will automatically remove the duplicate values.

obj= {1,"nitesh", 4.5, "nitesh"}
print(obj)  #it will remove another "nitesh" from the set.

set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}
print(set1.intersection(set2))
print(set1.union(set2))
print(set1.difference(set2))  


