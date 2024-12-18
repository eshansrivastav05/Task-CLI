import json
from datetime import *
from tabulate import tabulate

FILE_NAME = 'tasks list.json' #Set file name

#Function queries for the existing tasks and if the file does not exist it creates it
def read_tasks():
	try:
		with open(FILE_NAME, 'r') as tasks_list: #Locates and returns file data
			return json.load(tasks_list)
	except (FileNotFoundError, json.JSONDecodeError): #On error, an empty list returns
		return []

def find_task(task_id): #Finds a task based on id
	tasks = read_tasks()
	for task in tasks: #Iterates through each task to find similar id
		if task.get("id") == task_id:
			return task
	return False

def write_tasks(tasks): #Simple function that overwrites the json file
	with open(FILE_NAME, 'w') as tasks_list:
		json.dump(tasks, tasks_list) #Stores tasks into json file

def add_task(task_name): #Creates new tasks
	tasks = read_tasks()
	task_id = (datetime.now().strftime("%S%f")) #Creates id based on clock
	task_description = input('Enter some details about the task or press enter: ')
	task_details = { #Stores all task info into dictionary
		'id': task_id, 
		'name': task_name, 
		'description': task_description, 
		'status': 'todo', 
		'createdAt':datetime.now().strftime("%Y-%m-%d %H:%M"), 
		'updatedAt':datetime.now().strftime("%Y-%m-%d %H:%M")
	}
	tasks.append(task_details) #Stores the dictionary in a list
	write_tasks(tasks) #Stores list in json file
	print('Task has been added')

def delete_task(task_id): #Removes tasks
	tasks = read_tasks()
	task_to_delete = find_task(task_id) #Stores the task user wants to delete
	if task_to_delete == False:
		print('Task not found')
		return
	else:
		while True: #Asks user to confirm deletion
			user_confirmation = input(f'Do you want to delete {task_to_delete.get("name")}? (Y/N)')
			if user_confirmation == 'Y':
				tasks.remove(task_to_delete) #Removes dictionary of task from the list
				write_tasks(tasks) #Overwrites the json file
				print(f'{task_to_delete.get("name")} deleted')
				break
			if user_confirmation == 'N': #Ignores if the user changes their mind
				break
			else:
				continue #Continues to loop until the user makes a decision
			    
def update_task(task_id): #Changes a task's name and/or description
	tasks = read_tasks()
	task_to_update = find_task(task_id) #Extracts the one task to be updated
	if task_to_update == False: #Ends function if the task is not found
		print('Task not Found')
		return
	index = tasks.index(task_to_update) #Stores the index of the task
	
	#Asks user to update task properties
	updated_name = input('Enter a new name for the task or press enter: ')
	updated_description = input('Enter a new description for the task or press enter: ')
	
	#Will only update if one of the two are entered
	if updated_name != "":
		task_to_update['name'] = updated_name
	if updated_description != "":
		task_to_update['description'] = updated_description
	if (updated_name != "") or (updated_description != ""): #UpdatedAt will change to current time stamp if one of the two changes
		task_to_update['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M")
	
	tasks[index] = task_to_update #Places the updated task in the same position as the non_updated one
	write_tasks(tasks) #Puts task list back into json file
	print('Task Updated')

def update_task_status(status_change, task_id): #Changes the status property of a task
	
	tasks = read_tasks()
	task_to_update = find_task(task_id) #Extracts the one task to be updated
	if task_to_update == False: #Ends function if the task is not found
		print('Task not Found')
		return
	index = tasks.index(task_to_update) #Stores the index of the task
		
	#Changes the dictionary value based on the user input
	if status_change == 'mark-todo':
		task_to_update['status'] = 'todo'
	elif status_change == 'mark-in-progress':
		task_to_update['status'] = 'in-progress'
	elif status_change == 'mark-done':
		task_to_update['status'] = 'done'
	task_to_update['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M")
		
	tasks[index] = task_to_update #Places the updated task in the same position as the non_updated one
	write_tasks(tasks) #Puts task list back into json file
	print('Status Updated')

#Function will generate tables based on status
def generate_task_list(task_status = ""): #Status is set to none
	task_data = read_tasks()
	if task_status == "": #Creates a table with all tasks
		print(tabulate(task_data, tablefmt="grid"))
	
	#The program will iterate through all tasks and find the ones with the
	#requested status. The tasks with the status we are looking for are stored
	#in a temporary list and then used to generate a new table
	
	elif task_status == "todo":
		todo_tasks = []
		for task in task_data:
			if task.get('status') == "todo":
				todo_tasks.append(task)
		print(tabulate(todo_tasks, tablefmt="grid"))
	elif task_status == "in-progress":
		in_progress_tasks = []
		for task in task_data:
			if task.get('status') == "in-progress":
				in_progress_tasks.append(task)
		print(tabulate(in_progress_tasks, tablefmt="grid"))
	elif task_status == "done":
		done_tasks = []
		for task in task_data:
			if task.get('status') == "done":
				done_tasks.append(task)
		print(tabulate(done_tasks, tablefmt="grid"))
