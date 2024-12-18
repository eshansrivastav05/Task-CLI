from ToDo_List_Functions import *

def task_CLI_help(): #Function stores help information for user
	help_options = """
Available commands include:\n
add
update
mark-todo
mark-in-progress
mark-done
delete
list
list-todo
list-in-progress
list-done\n
exit
help
-help
--help
-h\n
Enter all commands in lower case\n
Enter the command name and the task index in the format <[command-name] [task-index]> for all commands except add, list commands, exit, and help
	"""
	return help_options

#List of eligible commands
help_commands = ['help', '-h', '--help', '-help']

if __name__ == '__main__':
	print('Welcome to Task CLI')
	while True: #Continuously loops
		try:
			user_command = input("task-cli >> ") #Keeps asking for user commands
			if user_command in help_commands: #Check whether user asked for help
				print(task_CLI_help()) #Prints help info
			elif user_command == 'exit': #Checks whether user wants to end session
				break #Ends while loop effectively ending the session
			
			
			#The following statements check whether the user's input contains a command
			#and will call the specific command if the user has entered it.
			#It will splice the user's input to find the task_id and various other info
			
			
			elif "add " in user_command:
				add_task(user_command[4:])
			elif "delete " in user_command:
				delete_task(user_command[7:])
			elif user_command == "list":
				generate_task_list()
			elif user_command == "list-todo":
				generate_task_list("todo")
			elif user_command == "list-in-progress":
				generate_task_list("in-progress")
			elif user_command == "list-done":
				generate_task_list("done")
			elif 'update ' in user_command:
				update_task(user_command[7:])
			elif 'mark-todo ' in user_command:
				update_task_status('mark-todo', user_command[10:])
			elif 'mark-in-progress ' in user_command:
				update_task_status('mark-in-progress', user_command[17:])
			elif 'mark-done ' in user_command:
				update_task_status('mark-done', user_command[10:])
			elif user_command == "":
				continue
			else:
				print("Command not found")
		except KeyboardInterrupt:
			print()
