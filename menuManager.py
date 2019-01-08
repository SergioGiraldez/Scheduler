# SCHEDULER by Sergi Giraldez

#imports
import sys, classContainer, fileManager, operator
from time import gmtime, strftime

"""  STRUCTURE
LOGIN                   MENU                                SCHEDULE
user field              New Schedule                        (Fields: Available Hours
pass field              (Subscreen the Schedules                List of tasks
Login                   listed.Remove, edit & run               (remove, postpone
                        Schedule options inside)                edit inside)
                        (SEND NEW TASK)?                    Add Task
register                Logout                              Back / Safe
"""


def showMenu():
    print(mainMenu)

def mainMenuRedirectTo(option):
    if option == 1:
        #crete schedule
        createSchedule()
    elif option == 2:
        #shows menu to edit schedule
        taskManager()
    elif option == 3:
        #recalc next task
        calcNextTask()
    elif option == 4:
        #shows menu to postpone a task
        postponeTask()

#Schedule functions
def createSchedule():
    #TODO: Safe in a logFile
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " - createSchedule() IN")

    #TODO: Introduce data to create Schedule

    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " - createSchedule() OUT")

def taskManager():
    #TODO: Safe in a logFile
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " - taskManager() IN")

    #TODO: new window task select

    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " - taskManager() OUT")

def modifTasks():
    pass
    #TODO: Needed? Here?

def loadSchedule():
    #TODO: Safe in a logFile
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " - loadSchedule() IN")

    #TODO: new window schedule select
    #DELETE: print("Wich one do you want to load?")
    fileNames = fileManager.showFileList()
    #DELETE: print("Write the number acording to the file:")
    nameIndex = int(input()) - 1
    info = fileManager.readScheduleFile(fileNames[nameIndex])
    if info == None:
        print("ERR: reading file")
    else:
        #TODO: HACER ESTO EN OTRA FUNCION
        for i in info.tasks:
            i.calcPriority(info.availableHours,info.totalDificulty,info.firstDate)

        info.tasks.sort(key= operator.attrgetter("priority"),reverse=False)

    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " - loadSchedule() OUT")

def calcNextTask():
    #TODO: Safe in a logFile
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " - modifSchedule() IN")

    #TODO: Send next highest prio task

    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " - modifSchedule() OUT")

def postponeTask():
    #TODO: Safe in a logFile
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " - modifSchedule() IN")

    #TODO: Window to select the task & how much time to postpone the task

    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " - modifSchedule() OUT")
