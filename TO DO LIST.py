import sys
def todo():
    query=input("What do you want to do \t type(1/2/3)?\n 1) ADD NEW TASK\n 2)VIEW ALL TASKS\n3) MARK  TASK AS COMPLETE\n")
    try:
        if int(query)==1:
            with open("tasks.txt","a+") as file:
                    file.seek(0)
                    project_no=len(file.readlines())+1
                    file.write(str(project_no)+") "+input("\n\nWhat is the new task?")+"\n")
                    print("Task added")
                    file.close()
        elif int(query)==2:
            with open("tasks.txt","r") as file:
                tasks=file.readlines()
                if len(tasks)==0:
                    print("NO TASKS AVAILABLE")
                else:
                    print("TASKS:\n")
                    for task in tasks:
                        if "COMPLETED" not in task:
                            print(task.strip())
                file.close()
        elif int(query)==3:
            with open("tasks.txt","r") as file:
                tasks=file.readlines()
                if len(tasks)==0:
                    print("NO TASKS AVAILABLE")
                    print("PLEASE ADD A TASK FIRST")
                else:
                    print("TASKS:\n")
                    for task in tasks:
                        print(task.strip())
            comp = input("\n\nwhich task did you complete? PROJECT NO=?\n")
            for idx, task in enumerate(tasks):
                if comp in task:
                    if "COMPLETED" not in task:
                        tasks[idx] = task.strip() + " ✔️ COMPLETED\n"
                        print("TASK MARKED AS COMPLETE")
                        break
                    else:
                        print("TASK ALREADY COMPLETED")
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
                file.close()
    except ValueError as e:
            print("PUT A VALID NUMBER :",e)
            sys.exit()





if __name__=="__main__":
      todo()
    