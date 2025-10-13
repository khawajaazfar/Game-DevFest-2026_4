# todo_list_manager.py

def show_menu():
    print("\n📋 To-Do List Manager")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

def todo_list():
    tasks = []
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            task = input("Enter a task: ")
            tasks.append(task)
        elif choice == '2':
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
        elif choice == '3':
            num = int(input("Enter task number to remove: "))
            if 0 < num <= len(tasks):
                tasks.pop(num-1)
        elif choice == '4':
            print("✅ Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    todo_list()
