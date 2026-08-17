def task_driven(task,task_add):
    task_add.append(task)
    return task_add
def task_delete(task_add):
    task_del=input("Enter the Task to be delete :")
    task_add.remove(task_del)
    return task_add
def task_view(task_add):
    view_task=print(f"All the task are {task_add}")
    return view_task

def main_driven():
    task_add=[]
    while True:
        choice=int(input("Enter the choice : \n 1.Add A new Task \n 2.Remove the Task \n 3.View all the task \n 4.Exit \n"))
        match choice:
            case 1:
                task=input("Enter the Task to be Add :")
                print(f"The tasks are:{task_driven(task,task_add)}")
            case 2:
                print(f"The tasks to remove :{task_delete(task_add)}")
            case 3:
                task_view(task_add)
            case 4:
                print("Exited ....Thank You...")
                break
main_driven()