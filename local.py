y=800    # global variable
def f1():
    x=90    # local variable
    print("My X value=",x)
    def f2():
       nonlocal x
       x=1000      #  non local variable
       print(x)
    f2()
    
f1()





