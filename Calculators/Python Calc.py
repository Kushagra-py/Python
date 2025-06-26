x = input("Press ANY key to start OR x to exit: ")
def loop():

 num1 = int(input("enter first number: "))
 num2 = int(input("enter second number: "))
 operator = input("select operator(+,-,*,/,**): ")

 if len(operator) > 2:
    print("Error!, only 1 operator allowed. choose from +,-,*,/,** only")
 elif operator == "+":
    print("sum is: ", num1 + num2)
 elif operator == "-":
    print("difference is: ", num1 - num2)
 elif operator == "*":
    print("Product is: ", num1 * num2)
 elif operator == "/":
    print("quotient is: ", num1 / num2)
 elif operator == "**":
    print("exponentation is: ", num1 ** num2)  
 else: 
    print("ERROR!, your function was", operator , "choose from +,-,*,/,** only")  

 x = input("Press ANY key to start OR x to exit: ")
 if x == "x":
    print("Thank you for using this calculator")     
 else:
    loop()

if x == "x":
     print("Script terminating. Goodbye.")
else:
    loop()
 
