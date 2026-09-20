import json
import os


FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("Warning: tasks.json is corrupted. Starting with an empty list.")
        return []

    except OSError as error:
        print(f"Error loading tasks: {error}")
        return []


def save_tasks(tasks):
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)

    except OSError as error:
        print(f"Error saving tasks: {error}")


def add_task(tasks):
    description = input("Enter task description: ").strip()

    if not description:
        print("Task cannot be empty.")
        return

    task = {
        "id": len(tasks) + 1,
        "description": description,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully.")


def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n" + "=" * 60)
    print("TO-DO LIST")
    print("=" * 60)

    for task in tasks:
        status = "✓ Done" if task["completed"] else "Pending"

        print(
            f'{task["id"]}. '
            f'{task["description"]} '
            f'[{status}]'
        )


def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_id = int(input("\nEnter task ID to delete: "))

    except ValueError:
        print("Please enter a valid task ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)

            # Reassign IDs
            for index, task in enumerate(tasks, start=1):
                task["id"] = index

            save_tasks(tasks)

            print("Task deleted successfully.")
            return

    print("Task does not exist.")


def mark_completed(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_id = int(input("\nEnter task ID to mark as completed: "))

    except ValueError:
        print("Please enter a valid task ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                print("Task is already completed.")
            else:
                task["completed"] = True
                save_tasks(tasks)
                print("Task marked as completed.")
            return

    print("Task does not exist.")


def show_menu():
    print("\n" + "=" * 40)
    print("          TO-DO LIST APPLICATION")
    print("=" * 40)
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")


def main():
    tasks = load_tasks()

    while True:
        show_menu()

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            mark_completed(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please select 1-5.")


if __name__ == "__main__":
    main()