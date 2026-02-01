To-do list(console)
# tasks = []

# while True:
#     print("\n===== TO-DO LIST MENU =====")
#     print("1. Add Task")
#     print("2. View Tasks")
#     print("3. Remove Task")
#     print("4.Exit")

#     choice = input("Enter your choice (1-4): ")

#     if choice == "1":
#         task=input("Enter a task: ")
#         tasks.append(task)
#         print("Task added sucessfully!")

#     elif choice == "2":
#         if len(tasks) == 0:
#             print("No tasks found.")
#         else:
#             print("\n your Tasks:")
#             for i in range(len(tasks)):
#                 print(f"{i+1}. {tasks[i]}")

#     elif choice == "3":
#         if len(tasks) == 0:
#             print("No tasks to remove.")
#         else:
#             print("\n Your Tasks:")
#             for i in range(len(tasks)):
#                 print(f"{i+1}. {tasks[i]}")

#             remove_task = int(input("Enter task number to remove: "))

#             if 1 <= remove_task <= len(tasks):
#                 removed = tasks.pop(remove_task -1)
#                 print(f"Removed task: {removed}")
#             else:
#                 print("Invalid task number!")

#     elif choice == "4":
#         print("exiting..Bye buddy!")
#         break
    
#     else:
#         print("Invalid choice! Please enter 1-4. ")
To-do list(console)
# tasks = []

# while True:
#     print("\n===== TO-DO LIST MENU =====")
#     print("1. Add Task")
#     print("2. View Tasks")
#     print("3. Remove Task")
#     print("4.Exit")

#     choice = input("Enter your choice (1-4): ")

#     if choice == "1":
#         task=input("Enter a task: ")
#         tasks.append(task)
#         print("Task added sucessfully!")

#     elif choice == "2":
#         if len(tasks) == 0:
#             print("No tasks found.")
#         else:
#             print("\n your Tasks:")
#             for i in range(len(tasks)):
#                 print(f"{i+1}. {tasks[i]}")

#     elif choice == "3":
#         if len(tasks) == 0:
#             print("No tasks to remove.")
#         else:
#             print("\n Your Tasks:")
#             for i in range(len(tasks)):
#                 print(f"{i+1}. {tasks[i]}")

#             remove_task = int(input("Enter task number to remove: "))

#             if 1 <= remove_task <= len(tasks):
#                 removed = tasks.pop(remove_task -1)
#                 print(f"Removed task: {removed}")
#             else:
#                 print("Invalid task number!")

#     elif choice == "4":
#         print("exiting..Bye buddy!")
#         break
    
#     else:
#         print("Invalid choice! Please enter 1-4. ")