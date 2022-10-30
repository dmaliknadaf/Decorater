def cap1(sentence):
    def inner():
        a = sentence()
        return a.upper()
    return inner

def cap2(sentence):
    def inner():
        b = sentence()
        return b.title()
    return inner
    
@cap2
@cap1

def sentence():
    return "hello how are you"
print(sentence())
