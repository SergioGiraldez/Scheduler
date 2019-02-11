import os, task


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
		read_tasks.append(task.Task(taskParams[0],taskParams[1],taskParams[2]))
	return read_tasks

#----------------------------------------------------------------------------------------
def get_first_date():
	return sorted(tasks, key = lambda task: task.date)[0].get_date_in_seconds()

#----------------------------------------------------------------------------------------
def get_files_in_directory():
	files = os.listdir('./user_resources')
	for positon,file in enumerate(files,1): #TODO: BORRAR ESTO
		print(positon,file)					#solo sirve para comprobacion
	return files
