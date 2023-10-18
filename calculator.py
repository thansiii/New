

a=input("Enter your Name")
print("Welcome Welcome Mr.",a)

def add(x,y):
    sum=x+y
    print(sum)

def sub(x,y):
    sub=x-y
    print(sub)    

def mul(x,y):
     mul=x*y
     print(mul)   

def div(x,y):
       div=x/y
       print(div)  



while True:
    x = float(input("Enter 1st number:"))
    y = float(input("Enter 2nd number:"))

    print("Choose an option: \n1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    option =int(input("Choose an option:"))

    if option == 1:
        add(x,y)


    elif option == 2:
        sub(x,y)
    elif option == 3:
       mul(x,y)

    elif option == 4:
       div(x,y)    
    else:
        print("OK")  

        
                