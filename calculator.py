


print("USE THE CALCULATOR FOR CALCULATION!!!!")

x=input("Press y/yes for calculation\n ")
while(x=="y" or x=="yes"):
    print("select + for addtion")       
    print("select - for subtraction")
    print("select * for multiplication")
    print("select / for normal division")
    print("select // for only integer of quotient")
    print("select % for only integer of quotient")

    sign=input("")
    if(sign=="+"):
        def add(x,y):
            return(x+y)
        x=int(input("Enter the value of x:\n"))
        y=int(input("Enter the value of y:\n"))
        s=add(x,y)
        print(s)
    
    elif(sign=="-"):
        def subtract(x,y):
            return(x-y)
        x=int(input("Enter the value of x:\n"))
        y=int(input("Enter the value of y:\n"))
        s=subtract(x,y)
        print(s)



    elif(sign=="*"):
        def multiply(x,y):
            return(x*y)
        x=int(input("Enter the value of x:\n"))
        y=int(input("Enter the value of y:\n"))
        s=multiply(x,y)
        print(s)


    elif(sign=="/"):
        def d1(x,y):
            return(x/y)
        x=int(input("Enter the value of x:\n"))
        y=int(input("Enter the value of y:\n"))
        s=d1(x,y)
        print(s)
        

    elif(sign=="//"):
        def d2(x,y):
            return(x//y)
        x=int(input("Enter the value of x:\n"))
        y=int(input("Enter the value of y:\n"))
        s=d2(x,y)
        print(s)



    elif(sign=="%"):
        def d3(x,y):
            return(x%y)
        x=int(input("Enter the value of x:\n"))
        y=int(input("Enter the value of y:\n"))
        s=d3(x,y)
        print(s)
    else:
        print("Invalid choice!!!")

    x=input("Do you waann to calculate again? yes/n\n")
    if(x=="no" or x=="n"):
        print("Thanks for using it...")
        break
