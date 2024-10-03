def func(greeting, Name):
    print(f"{greeting}. My name is {Name}.")
    
func("Namaste","Neetesh")


def func_tion(*args, **kwargs):
    print(args)
    print(kwargs)
func_tion("Math","Science","English",age=21,name="Nitesh",surname="Nepal")


courses=["Math", "Science"]
items={"Name":"Samrajya", "Surname":"Nepal"}
func_tion(*courses, **items)