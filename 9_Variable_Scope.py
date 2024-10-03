"""
#There are 4 types of Variable:
L= Local
E= Enclosed
G= Global
B= Built-in"""
"""import builtins
print(dir(builtins))



def maxii():
    print("K chha?")
maxii()


max_num= max([1,2,3,4,5,6])
print(max_num)

#1.
x= "Global x"
y="global y"
def var():
    #global x
    x= "Local x"
    print(x)
var()
print(x)
print(y)

#2.
def test(z):
    z="local k"
    print(z)
test("local z")

#3.
x="Global x"
def outer():
    x="outer x"
    def inner():
        #nonlocal x
        x="inner x"
        print(x)
    inner()
    print(x)
outer()
print(x)"""


x= "Global X"
def functionn(z):
    #x= "Local x"
    x= "Outer x"
    def inner(z):
        x= "Inner x"
        print(x)
    inner(z)
    print(x)

functionn(x)
print(x)
