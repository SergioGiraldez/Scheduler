import os, task

def get_users_registered():
	with open(".resources/users.txt", "rt") as file:
		users_from_file = get_user_names_and_passwords(file)
		return users_from_file

#----------------------------------------------------------------------------------------
def get_user_names_and_passwords(file):
	users = []
	for user_line in file:
		users.append(user_line)
	return users

#----------------------------------------------------------------------------------------
def read(file_name):
	with open(file_name, "rt") as file:
		file_content = get_content(file)
		return file_content

#----------------------------------------------------------------------------------------
def get_content(file):
	available_hours = int(file.readline())
	tasks = get_tasks(file)
	first_date = get_first_date()
	total_dificulty = sum(task.dificulty for task in tasks)
	return classContainer.Info(available_hours, tasks, first_date, total_dificulty)


def get_categories():
	pass
	#TODO: implement file reader for categories.

#----------------------------------------------------------------------------------------
def get_tasks(file):
	read_tasks = []
	for task in file:
		task_params = task.split("/")
		read_tasks.append(task.Task(taskParams[0],taskParams[1],taskParams[2]))
	return read_tasks

#----------------------------------------------------------------------------------------
def get_first_date():
	return sorted(tasks, key = lambda task: task.date)[0].get_date_in_seconds()

#----------------------------------------------------------------------------------------
def get_file_names():
	files = os.listdir('./user_resources')
	for positon,file in enumerate(files,1): #TODO: BORRAR ESTO
		print(positon,file)					#solo sirve para comprobacion
	return files
