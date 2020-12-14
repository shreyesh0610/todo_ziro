to_do_dict = {}

mainmenu_options = {
    "1" : "View To-Do List",
    "2" : "Create To-Do List",
    "3" : "Update To-Do List",
    "4" : "Delete To-Do List",
}

update_options = {
    "1" : "Title",
    "2" : "Description",
    "3" : "Due Date",
    "4" : "Priority",
    "5" : "Completed",
}

go_back_menu = "0. Go Back to Main Menu"

class ToDo:

    id = 0

    def __init__(self, title, description, due_date, priority):

        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.active_flag = False

        ToDo.id += 1
        self.id = str(ToDo.id)
    
    def __str__(self):
        return "\nHere are the details:"  + "\n\n"+ \
            "Title: " + self.title + "\n" + \
            "Description: " + self.description + "\n" + \
            "Due Date: " + self.due_date + "\n" + \
            "Priority: " + self.priority + "\n" + \
            "Completed: " + str(self.active_flag) + "\n"


def mainmenu():

    print("Please select one of the options: ")
    sorted(mainmenu_options)
    for mm_key, mm_value in mainmenu_options.items():
        print(mm_key + ". " + mm_value)

    mainmenu_input = input("Please enter your input: ")
    return mainmenu_input

def main():

    mainmenu_input = mainmenu()
    if mainmenu_input.strip() == "1": #View
        view_todo_list()
    elif mainmenu_input.strip() == "2": #Create
        create_todo_item()
    elif mainmenu_input.strip() == "3":#Update
        update_todo_list()      
    elif mainmenu_input.strip() == "4":#Delete
        delete_todo_list()      
    else:
        print ("Oops! You seem to have selected an invalid option.\n")


def create_todo_item():

    input_title = input("What would be the title of your To-Do: ")
    input_description = input("Okay. And the description: ")
    input_duedate = input('When is the due-date: (YYYY-MM-DD format): ')
    #year, month, day = map(int, date_entry.split('-'))
    #due_date = datetime.date(year, month, day)
    input_priority = input('Finally, the priority: ')

    to_do_item = ToDo(input_title,input_description, input_duedate, input_priority)
    print(to_do_item)

    #SAVE
    to_do_dict[str(to_do_item.id)] = to_do_item
    
    print ("Great!, I've saved your To-Do item\n")

def view_todo_list():

    if (len(to_do_dict) <= 0):
        print ("You do not have any to-do list. Please make a new one")
    else:
        print ("Here is your to-do list\n")
        temp_mapping = {}
        # for idx, todo_item in enumerate(to_do_dict, start = 1):
        #     temp_mapping = {str(idx) : str(list(todo_item.values())[0])}
        #     print(str(idx) + ". " + str(list(todo_item.values())[0].title))
        tempcount = 1
        for key, value in to_do_dict.items():
            temp_mapping[str(tempcount)] = str(key)
            print(str(tempcount) + ". " + str(value.title))
            tempcount +=1

        print(go_back_menu)
    
        todo_selected_no = input("Please enter the to-do item no. you would like to view else enter 0 to go back to main menu: ")

        if todo_selected_no == "0":
            mainmenu()
        elif todo_selected_no in temp_mapping:
            todo_to_view = to_do_dict[temp_mapping[todo_selected_no]]
            print(todo_to_view)
        else:
            print ("Oops! You seem to have selected an invalid to-do list. Please select a valid one\n")
            view_todo_list()

def update_todo_list():
    if (len(to_do_dict) <= 0):
        print ("You do not have any to-do list. Please make a new one")
    else:
        print ("Here is your to-do list\n")
        temp_mapping = {}

        tempcount = 1
        for key, value in to_do_dict.items():
            temp_mapping[str(tempcount)] = str(key)
            print(str(tempcount) + ". " + str(value.title))
            tempcount +=1

        print(go_back_menu)
    
        todo_selected_no = input("Please enter the to-do item no. you would like to update else enter 0 to go back to main menu: ")

        if todo_selected_no == "0":
            mainmenu()
        elif todo_selected_no in temp_mapping:
            todo_to_view = to_do_dict[temp_mapping[todo_selected_no]]
            
            print ("What would you like to update for the do to list?")

            for k,v in update_options.items():
                print (k + ". "+ v)
            print (go_back_menu)
            
            update_no = input("Please enter the option no: ")

            if update_no == "5":
                text = ""
                if (todo_to_view.active_flag):
                    text = "The item is marked completed. Would you like to revert it to pending?"
                else:
                    text = "The item is pending. Would you like to mark it completed?"

                print (text + "\n" + "1. Yes\n" + "2. No\n 3.Fo Back to Main Menu" )

                yesno_input = input("Please enter an option: ")

                if yesno_input.lower() in ['yes','1']:
                    todo_to_view.active_flag = not todo_to_view.active_flag
                    print ("Cool! It has been updated")
                elif yesno_input == "0":
                    mainmenu()
                else:
                    print ("No problem! I'll keep it as it is")
                

            else:

                updated_input = input("Sure, please provide the updated " + update_options[update_no] + ":")

                if update_no == "1":
                    todo_to_view.title = updated_input
                elif update_no == "2":
                    todo_to_view.description = updated_input
                elif update_no == "3":
                    todo_to_view.due_date = updated_input
                elif update_no == "4":
                    todo_to_view.priority = updated_input
                elif update_no == "0":
                    mainmenu()
                print ("Cool! It has been updated")

                
            to_do_dict[str(todo_to_view.id)] = todo_to_view

        else:
            print ("Oops! You seem to have selected an invalid to-do list. Please select a valid one\n")
            view_todo_list()

def delete_todo_list():
    if (len(to_do_dict) <= 0):
        print ("You do not have any to-do list. Please make a new one")
    else:
        print ("Here is your to-do list\n")
        temp_mapping = {}

        tempcount = 1
        for key, value in to_do_dict.items():
            temp_mapping[str(tempcount)] = str(key)
            print(str(tempcount) + ". " + str(value.title))
            tempcount +=1

        print(go_back_menu)
    
        todo_selected_no = input("Please enter the to-do item no. you would like to delete else enter 0 to go back to main menu: ")

        if todo_selected_no == "0":
            mainmenu()
        elif todo_selected_no in temp_mapping:
            todo_to_view = to_do_dict[temp_mapping[todo_selected_no]]
               
            to_do_dict.pop(str(todo_to_view.id))
            print ("Cool!. The item has been deleted")

        else:
            print ("Oops! You seem to have selected an invalid to-do list. Please select a valid one\n")
            view_todo_list()    

while (True):
    main()

