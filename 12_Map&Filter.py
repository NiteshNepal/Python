nums=[1,2,3,4,5,6,7,8,9,0]

list_compre= list(map(lambda n : n%2==0, nums))
print(list_compre)

list_compre= list(filter(lambda n : n%2==0, nums))
print(list_compre)


list_comp= list(filter(lambda n: n%3==0 and n!=0, nums))
print(list_comp)

ll=list(filter(lambda n : n!=0 and n%2==0 and n!=2, nums))
print(ll)


    