#----------------------------------------------------------------------------------------
def write(info, file_name):
	file_name = convert_to_txt_file(file_name)
	if(file_exists(file_name)):
		ask_for_ovewriting(info, file_name)
	else:
		write_file_content(info, file_name)

#----------------------------------------------------------------------------------------
def convert_to_txt_file(file_name):
	if(len(file_name) < 5 or ".txt" == fn[-4:]):
		file_name += ".txt"
	return file_name

#----------------------------------------------------------------------------------------
def file_exists(file_name):
	return True if os.path.isfile(file_name) else False

#----------------------------------------------------------------------------------------
def ask_for_ovewriting():
    #show dialog message (file already exists want to overwrite?)
    print("a")

#----------------------------------------------------------------------------------------
def write_file_content(info, file_name):
    with open(file_name, "w") as file:
        file.write(info.availableHours)
        write_tasks(file, info)

#----------------------------------------------------------------------------------------
def write_tasks(file, info):
    for task in info.tasks:
        file.write(task.name + "/" + task.dificulty + "/" + task.date)
