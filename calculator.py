
def greet():
   g= input("do u want to use the calculator:") 

   if (g == "no"):
       a = print ("Thankyou for using")
       return a 
   else:
     return g

while (greet() == "yes" ):
    
    try:
      Num1 = int(input("Enter the 1st number:"))
      Num2 = int(input("Enter the 2nd number:"))

    except ValueError:
        print ("Invalid")

    else:
        i =  input("enter the operator:")
        if(i== "-" ):
           print("Num1 - Num2 =", Num1 - Num2)
        elif(i== "+"):
           print("Num1 + Num2 =", Num1 + Num2)
        elif(i == "*"):
           print("Num1 * Num2 =", Num1 * Num2)
        elif(i=="/"):
           print("Num1 / Num2 =", Num1 / Num2)
        elif(i=="%"):
           print("Num1 % Num2 =", Num1*100/Num2)
        else:
           print("Operator not found")
 


    

    
 

    


