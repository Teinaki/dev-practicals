"""Answer the questions below using the LEGB rule."""


num = 7

def func():
    count = 10
    def print_seven():
        extra = 2
        for _ in range(count + extra): # A
            print(num) # B
    return print_seven

f = func()
f()

# Answer the questions below.

#Q1: At the line marked A, describe how the interpreter finds the name count.
    #interpreter looks locally, count isn't there so it looks in enclosing for print_seven() it isn't there so it looks up a level in the enclosing func() to find count
#Q2: At the line marked A, describe how the interpreter finds the name extra.
    #interpreter looks locally, extra isn't there so it looks in enclosing for print_seven() to find extra
#Q3:  At the line marked B, describe how the interpreter finds the name num.
    #interpreter looks locally, num isn't there so it looks in enclosing for print_seven() it isn't there so it looks up a level in the enclosing func() also no there so it looks
    #globally to find num
