def decor(fun):
    def inner(name):
        if name == "Ravi":
            print("Hello Ravi bad morning")
        else:
            fun(name)
    return inner

@decor
def wish(name):
    print("Hello", name , "Good morning")

wish("Ravi")
wish("Sagar")
wish("Rahul")

