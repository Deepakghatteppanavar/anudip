# global variable
a = 10


def fun():
    # local variable
    b = 20
    print(a)
    print(b)


fun()
# ------------------------------------------------------------------------------------
# using same variable name
def fun1():
    a = 30

    # using same name local variable
    a = 40
    print(a)



fun1()

