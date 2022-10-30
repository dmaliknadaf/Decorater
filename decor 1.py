#manually
def second(paramtr):
    def inner():
        print("we still havent enahnced th function")
        paramtr()
        print("We have enhancd the function")
    return inner

def first():
    print("this line is before enhancing function")

third=second(first)
third()

#Using @
def second(first):
    def inner():
        print("we still havent enahnced the function")
        first()
        print("We have enhancd the function")
    return inner
@second
def first():
    print("this line is before enhancing function")
first()