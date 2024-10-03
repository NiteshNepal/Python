nums=[1,2,3,4,5,6,7,8]

#1.
my_list=[]
for n in nums:
    my_list.append(n)
print(my_list)
    
list_comp=[n for n in nums]  #list comprehension
print(list_comp)

#2.
my_list=[]
for n in nums:
    my_list.append(n*n)
print(my_list)

list_comp=[n*n for n in nums]
print(list_comp)

#3.
nums=[1,2,3,4,5,6,7,8,0]
list1=[]
for n in nums:
    if n%2==0:
        list1.append(n)
    else:
        continue
print(list1)

list_comp=[n for n in nums if n%2==0 and n!=0]
print(list_comp)


#4.
my_list=[]
for letter in 'abcd':
    for num in range(4):
        my_list.append((num,letter))
print(my_list)

my_list= [(num, letter) for letter in "abcd" for num in range(4)]
print(my_list)

#5.
name=["Nitesh", "Prateek","Marie", "Gold"]
superhero=["Ironman", "Spiderman", "Batman", "Superman"]

my_dict={}
for name, superhero in zip(name,superhero):
    my_dict[name]=superhero
print(my_dict) 

my_dict= {names : superheros for names, superheros in zip(name, superhero)}
print(my_dict)


movies= ["Inception", "Intersteller", "Shutter Island", "The Martian"]
char= ["Abbb", "Baaa", "Cddd", "Dccc"]
dicti={}
for movie,chars in zip(movies,char):
    dicti[movie]=chars
print(dicti)

list_com= {movie : chars for movie,chars in zip(movies,char)}
print(list_com)

list_comp= [n for n in nums if n%2!=0]
print(list_comp)

