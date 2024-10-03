items= ['book', "medicine", "phone", "Hotcase"]

"""for index, item in enumerate(items,start=0):
    print(index,item)"""
    
#break statement helps to break out of the loop instantly after the loop satisfy the mentioned condition.
for item in items:
    if item == "phone":
        print("You found Phone.")
        break
    print(item)

#continue statement helps to keep renning the the loop even after the loop satisfy the mentioned condition.
items=[1,2,3,4,5,6,7,8,9]
for item in items:
    if item==3:
        print("Valid Found")
        continue
    print(item)
    
"""     
for i in range(0,20):
    if i == 10:
        break
    print(i)"""

"""x=0
while x <= 10:
    
    print(x)
    x+=1"""
  