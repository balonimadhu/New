user_name=str(input("enter user name:"))
print("Hello", user_name +  "Welcome to the calculater application")
print("Select an operation to perform:")
print("1. ADD")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
operation= input()
try:
   if operation == "1":
    num1=int(input("enter your first number:"))
    num2=int(input("enter your second number:"))
    print("the sum is" + str (int(num1)+int(num2)))
   elif operation =="2":
     num1=int(input("enter your first number:"))
     num2=int(input("enter your second number:"))
     print("the subtract is" + str (int(num1)-int(num2)))
   elif operation == "3":
     num1=int(input("enter your first number:"))
     num2=int(input("enter your second number:"))
     print("the Multiply is" + str (int(num1)*int(num2)))
   elif operation=="4":
     num1=int(input("enter your first number:"))
     num2=int(input("enter your second number:"))
     print("the divide is" + str (int(num1)/int(num2)))
   elif operation=="5":
     num1=int(input("enter your first number:"))
     num2=int(input("enter your second number:"))
     print("the Modulus is" + str (int(num1)%int(num2)))    
   else:
    print("Invalid Entry")
except ValueError:
         print("value error") 
      
 