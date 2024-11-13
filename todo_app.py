Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def first():
...   print("WELCOME TO THE TO-DO APPLICATION")
... 
... task1=[]
... time_taken=[]
... 
... first()
... total_task=int(input("enter the number of tasks you want to include: "))
... for i in range(1,total_task,):
...   task_name=input(f"enter the task {i}:")
...   task1.append(task_name)
...   time=int(input("enter the estimated time in minutes: "))
...   time_taken.append(time)
... 
...   
... print("YOUR TO DO LIST FOR TODAY IS: ")
... print(f"TASK: {task1}  TIME ESTIMATED: {time_taken}")
...   
... 
... def show_menu():
...   """MENU FOR THE USER"""
...   print("You can perform the following operations:")
...   print("1.Add task to existing task")
...   print("2.view task")
...   print("3.delete task")
...   print("4.Exit")
... 
... def main():
...  while True:
...    clear_screen()
...    show_menu()
...    choice=get_input("Enter your choice(1/2/3/4)")
... 
... 
...    if choice=="1":
...     task=get_input("enter the task to add:")
...     add_task(task)

   elif choice=="2":
    view_task()

   elif choice=="3":
    try:
     index = int(get_input("Enter the task index to delete: "))
     delete_task(index)
    except ValueError:
      print("please enter a valid position")

   elif choice=="4":
     print("EXITING THE TO-DO APP!!")
