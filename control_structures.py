# Programming with control structures
def classify_number():
  num=int(input("enter a number to classify: ")) #asking input from the user
  if num>0:
    print("positive")
  elif num<0:
    print("negative")
  else:
    print("zero")

a=input("enter 'exit' to exit: ") #to store something in 'a' before running the loop
while a!="exit":
  classify_number() #calling the function
  a=input("enter 'exit' to exit") #written twice because we need to show this statement in loop until user enters exit
