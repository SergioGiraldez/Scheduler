# SCHEDULER by Sergi Giraldez

#imports
import time, os, classContainer
from datetime import datetime


""" reads the file cointaining all the tasks to do and the hours available per day
	and returns an object with all the data.
	default file name: tasks.txt
"""
def readScheduleFile(fileName = "tasks.txt"):
	myTasks = []
	availableHours = 0
	firstDate = int(round(datetime(2025,11,20).timestamp()))
	totalDificulty = 0

	if os.path.isfile(fileName):
		try:
			#reads a text file
			f = open(fileName, "rt")
			try:
				#FIXME: PROBAR SI OPEN DEVUELVE ARRAY DE LINES

				#first file line is hours available per day
				availableHours = int(f.readline())

				#fills the tasks structure from file
				for x in f:
					taskParams = x.split("/")
			 		#param1: name param2: dificulty param3: date
					task = classContainer.Task(taskParams[0],taskParams[1],taskParams[2])
					myTasks.append(task)
					totalDificulty += int(task.dificulty)
					if task.getDateInSeconds() < firstDate:
						firstDate = task.getDateInSeconds()

				return classContainer.Info(availableHours, myTasks, firstDate, totalDificulty)

			finally:
				f.close()
		except IOError:
			print("Something went wrong when writing file: " + fileName)
			return None


""" creates a file with the info given.
	if an error ocurs the function returns 1,
	if there is no error the function returns 0
"""
def writeScheduleFile(info, fileName):
	fn = fileName
	#make it a text file if not specified by the user
	if(len(fn) < 5 or ".txt" == fn[-4:]):
		fn += ".txt"
	#if the file exists asks for a new name or to overwrite it
	if os.path.isfile(fn):
		fn = overwriteFile(fn)
	try:
		#opens file in write mode
		file = open(fn,"w")
		try:
			#first file's line is daily available hours
			file.write(info.availableHours)
			#secondo line and on, one task per line
			for x in info.tasks:
				file.write(x.name+"/"+x.dificulty+"/"+x.date) #TODO: Comprobar nombres de las variables de info

			#returns 0 if the operation is succesful
			return 0
		finally:
			file.close()
	except IOError:
		print("Something went wrong when writing file: " + fileName)
		#returns 1 if the operation had an error
		return 1


""" asks for a file name till it does not exist
	or the user wants to overwrite it.
	returns the file name
"""
def overwriteFile(fileName):

	fn = fileName
	end = 0

	#loops till a valid fileName is found
	while end == 0:
		print("The file "+fn+" exists, do you want to overwrite it?(Y/N)")
		validAnswer = 0
		#loops till the user answers Y or N
		while validAnswer == 0:
			x = input()
			#returns an existing file name to overwrite
			if x.lower() == 'y':
				validAnswer = 1
				end = 1
			#asks for a new file name
			elif x.lower() == 'n':
				validAnswer = 1
				print("Introduce a new file name:")
				fn = input()
				#make it a text file if not specified by the user
				if(len(fn) < 5 or ".txt" == fn[-4:]):
					fn += ".txt"
				#ends the loop if new file name does not exist
				if not os.path.isfile(fn):
					end = 1
			else:
				print("Write Y if you want to overwrite it or N if you don't.")
	return fn

def showFileList():
	listOfFiles = os.listdir('.')
	for x,entry in enumerate(listOfFiles,1):
		print(x,entry)
	return listOfFiles
