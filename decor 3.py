
#manually
def decor1(fun):
    def inner():
        a = fun()
        multi = a * 5
        return multi
    return inner

def decor2(fun):
    def inner():
        b = fun()
        add = b + 5
        return add
    return inner

def num():
    return 10

num = decor2(decor1(num))
print(num())


#Using @
def decor1(num):
    def inner():
        a = num()
        multi = a * 5
        return multi
    return inner
def decor2(num):
    def inner():
        b = num()
        add = b + 5
        return add
    return inner
@decor2
@decor1
def num():
    return 10

print(num())