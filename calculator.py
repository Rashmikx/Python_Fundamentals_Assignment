#creating four different functions
def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    if y==0:              
        return "this operation cannot be performed"
    else:
        return x/y

print("Select operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")

choice = input("Enter choice(1/2/3/4/5): ")

if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
elif choice=='5':
      print("Exiting")
else:                           
        print("Invalid Input")


if choice == '1':
  result=addition(num1,num2)
  print(f"sum= {result}")
if choice == '2':
  result=subtraction(num1,num2)
  print(f"difference= {result}")
if choice == '3':
  result=multiplication(num1,num2)
  print(f"product= {result}")
if choice == '4':
  result=division(num1,num2)
  print(f"quotient= {result}")
