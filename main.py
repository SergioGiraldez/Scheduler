# SCHEDULER by Sergi Giraldez

#imports
import sys, scheduler, fileManager, operator

mainMenu = "******************** MENU ********************\n 1. New Schedule.\n 2. Edit tasks.\n 3. Give me a task.\n 4. Manage tasks.\n 5. Load existing Schedule.\n 6. Exit"
editTaskMenu = "****************** EDIT TASK ******************\n 1. Add new task.\n 2. Remove existing task.\n 3. View task info.\n 4. Return to Menu."
manageTaskMenu = "***************** MANAGE TASK *****************\n 1. Give me a task.\n 2. Postpone a task.\n 3. Return to Menu."
wrongOp = "Wrong option, select again."

def showMenu():
    print(mainMenu)

def mainMenuRedirectTo(option):
    if option == 1:
        #crete schedule
        createSchedule()
    elif option == 2:
        #shows menu to edit schedule
        modifSchedule()
    elif option == 3:
        #recalc next task
        calcNextTask()
    elif option == 4:
        #shows menu to postpone a task
        postponeTask()
    elif option == 5:
        #shows menu to load an existing schedule
        loadSchedule()
        #TODO: THREAD QUE CADA HORA RECALCULE TAREA
    elif option == 6:
        #closes the program
        print("thanks for using Schedule!")
        sys.exit()
    else:
        print(wrongOp)

#Schedule functions
def createSchedule():
    print("Name your schedule:")
def modifSchedule():
    print("Wich one do you want to edit?")
    #TODO: PRINT SCHEDULE FILE LIST TO CHOOSE.
    #TODO: OPTION TO MODIF TASKS
def modifTasks():
    print("Wich task do you want to edit?")
    #TODO: PRINT TASK LIST TO CHOOSE.
def loadSchedule():
    print("Wich one do you want to load?")
    fileNames = fileManager.showFileList()
    print("Write the number acording to the file:")
    nameIndex = int(input()) - 1
    info = fileManager.readScheduleFile(fileNames[nameIndex])
    if info == None:
        print("Something went wrong. (MAIN)")
    else:
        #TODO: HACER ESTO EN OTRA FUNCION
        for i in info.tasks:
            print(i.name)
            i.calcPriority(info.availableHours,info.totalDificulty,info.firstDate)

        info.tasks.sort(key= operator.attrgetter("priority"),reverse=False)
        for i in info.tasks:
            print(i.name)

def calcNextTask():
    print("Calculating next task to do ...")
    #TODO: MAKE THE MATHS
def postponeTask():
    print("Select a the task you want to postpone: ")
    #TODO: PRINT A LIST OF THE TASKS


#Element showing functions

# Program start function
def main():
    end = 0
    while end == 0:
        showMenu()
        option = int(input())
        mainMenuRedirectTo(option)

#FIXME: FER README
if __name__ == '__main__':
    main()
