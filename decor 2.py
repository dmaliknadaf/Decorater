#manually
def decor(fun):
    def inner():
        a = fun()
        add = a + 10
        return add
    return inner

def num():
    return 10

call_decor = decor(num)
print(call_decor())

#Using @
def decor(fun):
    def inner():
        a = fun()
        add = a + 10
        return add
    return inner
@ decor
def num():
    return 10

print(num())