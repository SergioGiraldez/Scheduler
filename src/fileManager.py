# SCHEDULER by Sergi Giraldez

#imports
import time, os, classContainer
from datetime import datetime


def read_file(file_name):
	with open(file_name, "rt") as file:
		file_content = read_file_content(file)
		return file_content

#----------------------------------------------------------------------------------------
def read_content_from_file(file):
	available_hours = int(file.readline())
	tasks = read_tasks_from_file(file)
	first_date = get_first_date()
	total_dificulty = sum(task.dificulty for task in tasks)
	return classContainer.Info(available_hours, tasks, first_date, total_dificulty)

#----------------------------------------------------------------------------------------
def read_tasks_from_file(file):
	read_tasks = []
	for task in file:
		task_params = task.split("/")
		read_tasks.append(classContainer.Task(taskParams[0],taskParams[1],taskParams[2]))
	return read_tasks

#----------------------------------------------------------------------------------------
def get_first_date():
	return sorted(tasks, key = lambda task: task.date)[0].get_date_in_seconds()

#----------------------------------------------------------------------------------------
def write_file(info, file_name):
	file_name = convert_to_txt_file(file_name)
	if(file_exists):
		ask_for_new_name()
	else:
		write_file_content(info, file_name)

#----------------------------------------------------------------------------------------
def convert_to_txt_file(file_name):
	if(len(file_name) < 5 or ".txt" == fn[-4:]):
		file_name += ".txt"
	return file_name

#----------------------------------------------------------------------------------------
def file_exists(file_name):

	if os.path.isfile(fn):


def ask_for_new_name():


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

def show_file_list():
	listOfFiles = os.listdir('.')
	for x,entry in enumerate(listOfFiles,1):
		print(x,entry)
	return listOfFiles
