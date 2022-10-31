def smart_division(fun):
    def inner(a,b):
        print("we are dividing" ,a, "with" ,b)
        if b==0:
            return ("OOPS... cannot divide by zero")
        else:
            return fun(a,b)
    return inner
@smart_division

def division(a,b):
    return a/b

print(division(20,2))
print(division(20,0))