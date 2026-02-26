import json
import emoji

Menu = "\n==== To Do List ====\n\n1. View tasks\n2. Add task\n3. Mark task as done\n4. Delete task\n5. Exit\n\nChoose an option: "

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except:
        return []

tasks = load_tasks()
while True:
    Choice = int(input(Menu))

    if Choice == 1:
        if not tasks:
            print("no tasks yet!")
        else:
            for i, task in enumerate(tasks, start=1):
                emojii = ":cross_mark:" if task["done"] == False else ":check_mark_button:"
                print(emoji.emojize(f"{i}- {task["title"]} {emojii}"))

    elif Choice == 2:
        title = input("Enter the new task's name: ")
        new_task = {
        "title": title,
        "done": False
        }
        tasks.append(new_task)
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)
        
    elif Choice == 3:
        n = int(input("Enter the task's number to mark it as done: "))
        tasks[n - 1]["done"] = True
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)

    elif Choice == 4:
        n2 = int(input("Enter the task's number to delete it: "))
        del tasks[n2 - 1]
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)

    elif Choice == 5:
        break
    else:
        print("Please enter a number between 1-5")