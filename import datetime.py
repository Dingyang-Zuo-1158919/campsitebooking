# ============== Selwyn Campground MAIN PROGRAM ==============
# Student Name: Dingyang Zuo
# Student ID : 1158919
# NOTE: Make sure your two files are in the same folder
# =================================================================================

import camp_data    # camp_data.py MUST be in the SAME FOLDER as this file!
                    # camp_data.py contains the data
import datetime     # We are using date times for this assessment, and it is
                    # available in the column_output() function, so do not delete this line
import re

# Data variables
#col variables contain the format of each data column and help display headings
#db variables contain the actual data
col_customers = camp_data.col_customers
db_customers = camp_data.db_customers
col_bookings = camp_data.col_bookings
db_bookings = camp_data.db_bookings
UNPS = camp_data.UNPS #list of unpowered sites
PS = camp_data.PS #list of powered sites


def next_id(db_data):
    #Pass in the dictionary that you want to return a new ID number for, this will return a new integer value
    # that is one higher than the current maximum in the list.
    return max(db_data.keys())+1

def column_output(db_data, cols, format_str):
    # db_data is a list of tuples.
    # cols is a dictionary with column name as the key and data type as the item.
    # format_str uses the following format, with one set of curly braces {} for each column:
    #   eg, "{: <10}" determines the width of each column, padded with spaces (10 spaces in this example)
    #   <, ^ and > determine the alignment of the text: < (left aligned), ^ (centre aligned), > (right aligned)
    #   The following example is for 3 columns of output: left-aligned 5 characters wide; centred 10 characters; right-aligned 15 characters:
    #       format_str = "{: <5}  {: ^10}  {: >15}"
    #   Make sure the column is wider than the heading text and the widest entry in that column,
    #       otherwise the columns won't align correctly.
    # You can also pad with something other than a space and put characters between the columns, 
    # eg, this pads with full stops '.' and separates the columns with the pipe character '|' :
    #       format_str = "{:.<5} | {:.^10} | {:.>15}"
    print(format_str.format(*cols))
    for row in db_data:
        row_list = list(row)
        for index, item in enumerate(row_list):
            if item is None:      # Removes any None values from the row_list, which would cause the print(*row_list) to fail
                row_list[index] = ""       # Replaces them with an empty string
            elif isinstance(item, datetime.date):    # If item is a date, convert to a string to avoid formatting issues
                row_list[index] = str(item)
        print(format_str.format(*row_list))


def list_customers():
    # List the ID, name, telephone number, and email of all customers

    # Use col_Customers for display
   
    # Convert the dictionary data into a list that displays the required data fields
    #initialise an empty list which will be used to pass data for display
    display_list = []
    #Iterate over all the customers in the dictionary
    for customer in db_customers.keys():
        #append to the display list the ID, Name, Telephone and Email
        display_list.append((customer,
                             db_customers[customer]['name'],
                             db_customers[customer]['phone'],
                             db_customers[customer]['email']))
    format_columns = "{: >4} | {: <18} | {: <15} | {: ^12}"
    print("\nCustomer LIST\n")    # display a heading for the output
    column_output(display_list, col_customers, format_columns)   # An example of how to call column_output function

    input("\nPress Enter to continue.")     # Pauses the code to allow the user to see the output



def list_campsites():
    # List the identifier, occupancy
    
    #merge UNPS and PS for sorting
    unordered_list = []
    unordered_list.extend(PS)
    unordered_list.extend(UNPS)
    ordered_list = sorted(unordered_list, key = lambda x: (x[0], x[1]))

    #create column dictionary and format rule for display campsites in column_output method
    col_PS = {'site identifier':str, 'maximum occupancy':int}
    format_list_campsites = "{:^15} | {:^15} "
    print("\nAVAILABLE CAMPSITES LIST\n")
    column_output(ordered_list, col_PS, format_list_campsites)

    input("\nPress Enter to continue.")


#preparation before build function(list campers by date)
#create regular expression method to check user input format of date
def reg_exp_check(date):
    pattern = "^\\d{4}\,\\d{1,2}\,\\d{1,2}$"
    if re.match(pattern,date):
        return True
    else:
        return False

def list_campers_by_date():
    # List the Date, name, site, occupancy
    #get date input, use regexp function to check format
    while True:
        try:
            date_select = input("Please enter the date in year,month,day (comma between three parameters) format: ")
            if reg_exp_check(date_select) == False:
                raise TypeError
            break
        except TypeError:
            print("Please enter the date in correct format: ")
    
        date_format = "%Y,%m,%d"
        date_choice = datetime.datetime.strptime(date_select,date_format)
        date_obj = date_choice.date()
    #create target list to store information for display
    #if date not exists in db_bookings, created a new tuple to with date and None(to indicate name, site, occupancy)
        target_list = []
        if date_obj in db_bookings.keys():
            merge_l = sum(db_bookings[date_obj], [])
            for i in range(0,len(merge_l)):
                target_list.append([date_obj, merge_l[i][0], db_customers[merge_l[i][1]]['name'] , merge_l[i][2]])
                #sort list by site identifier
                target_list.sort(key= lambda x : x == str(merge_l[i][0]))
        else:
            target_list.append([date_obj, None,None,None])

    #edit display format
    print("\nCAMPERS LIST BY DATE\n")
    col_list_campers = {'Date':str, 'Site':str, 'Name':int, 'Occupancy':int}
    format_list_campers = "{:^10} | {:^4} | {:^20} | {:^2} "
    column_output(target_list, col_list_campers, format_list_campers)
    
    input("\nPress Enter to continue.")

def add_customer():
    # Add a customer to the db_customers database, use the next_id to get an id for the customer.
    # Remember to add all required dictionaries.

    #create new list to store user inputs of new customer data
    new_name = str(input("please enter a new name: "))
    new_email = str(input("please enter a new email: "))
    new_phone = str(input("please enter a new phone number: "))
    new_l = {'name':new_name, 'email': new_email, 'phone': new_phone}
    id_num = next_id(db_customers)
    db_customers[id_num] = new_l
    print("you have successfully registered, your id is "+ str(id_num))

    input("\nPress Enter to continue.")

#Preparation before building add_booking method(create isAvailable functions)
    
#check booking availability by the selected site, date, occupants
def isAvailable(your_site, your_date, your_occu):
    #merge campsites list, will use it to check occupants later
    camp_list = []
    camp_list.extend(PS)
    camp_list.extend(UNPS)

    #if the user input date has no booking information exist, check if the input occupants is greater than max occupants, get availability bool result
    if your_date not in db_bookings.keys():
        for i in range(len(camp_list)):
            if camp_list[i][0] == your_site:
                result_occu1 = (int(camp_list[i][1]) - int(your_occu)) >= 0
                return result_occu1
        
    #if the user input date has some booking information existing, check if it is the site of user input 
    else:
        result_site_check = any(your_site in x[0] for x in db_bookings[your_date])
    #user input site at selected date has been booked
        if result_site_check == True:
            return False
    #if site of user input has not been booked, check if max occupants is available
        else:
            for i in range(len(camp_list)):
                if camp_list[i][0] == your_site:
                    result_occu2 = (int(camp_list[i][1]) - int(your_occu)) >= 0
                    return result_occu2
    
    
def add_booking():
    #get user id and name, check input validity(if exists or not, and if name&id are matched)
    while True:
        try:
            entered_id = input("Please enter your id: ")
            res = int(entered_id) in db_customers.keys()
            if res == False:
                raise ValueError
            break
        except ValueError:
            print("your id is not existed, please re-enter or go back to create a new account ")

    while True:
        try:
            entered_name = input("Please enter your name: ")
            if db_customers[int(entered_id)]['name'] != entered_name:
                raise ValueError
            break
        except ValueError:
            print("your name is not matched with your entered id, please re-enter: ")

    #get date input from user and check validity
    while True:
        try:
            entered_year = int(input("Please enter the year of your check-in: (must be equal or greater than current year)"))
            if entered_year < datetime.datetime.today().year:
                raise ValueError
            break
        except ValueError:
            print("The year you input is not valid, Please re-enter: ")
    while True:
        try:
            entered_month = int(input("Please enter the month of your check-in: (must be in range of 1 ~ 12)"))
            if entered_month < 1 or entered_month > 12:
                raise ValueError
            break
        except ValueError:
            print("The month you input is not valid, Please re-enter: ")
    while True:
        try:
            entered_day = int(input("Please enter the day of your check-in: (must be in range of 1 ~ 31)"))
            if entered_day < 1 or entered_day > 31:
                raise ValueError
            break
        except ValueError:
            print("The day you input is not valid, Please re-enter: ")

    entered_date = datetime.date(entered_year,entered_month,entered_day)
    if entered_date < datetime.date.today():
        print("Please re-enter a valid date. ")
        
    #show all camp site lists
    print("Please choose from the below camp sites: ")
    show_list = []
    for x in range(len(UNPS)):
        show_list.append(UNPS[x][0])
    for y in range(len(PS)):
        show_list.append(PS[y][0])
    print(show_list)

    #get site input and check the validity
    while True:
        try:
            entered_site = input("Please enter your site choice: ")
            if entered_site not in show_list:
                raise ValueError
            break
        except ValueError:
            print("the site you entered is not existing, please re-enter a campsite: ")

    #get user occupants, check input validity
    while True:
        try:
            entered_occu = input("Please enter your occupants: ")
            campsite_list = PS + UNPS
            for x in range(len(campsite_list)):
                if campsite_list[x][0] == entered_site:
                    site_max_occu = campsite_list[x][1]
            if int(entered_occu) <= 0 or int(entered_occu) > int(site_max_occu):
                raise ValueError
            break
        except ValueError:
            print("Please enter an integer number within max occupants of your selected camp site ")

    #get user staying days, check input validity
    while True:
        try:
            entered_stay = int(input("Please enter days you want to stay: (5 days max) "))
            if entered_stay> 5 or entered_stay < 1:
                raise ValueError
            elif type(entered_stay) != int:
                raise TypeError
            break
        except ValueError:
            print("The day number you entered is incorrect, please re-enter a valid number: (max 5)")
        except TypeError:
            print("Your input is not a number, please re-enter: (5 days max)")
    
    #check each of user staying day's availability by calling isavailable function
    #list_1 (seperate and store user staying days)
    #list_2 (store bool results for booking availability of each user staying day)
    list_1 = []
    list_2 = []
    for i in range(0, entered_stay):
        list_1.append(entered_date + datetime.timedelta(days = i))
        new_l = (int(list_1[i].strftime("%Y")), int(list_1[i].strftime("%m")), int(list_1[i].strftime("%d")))
        list_2.append(isAvailable(entered_site, datetime.date(*new_l), entered_occu))
    stay_result = False not in list_2

    #if booking available, add booking information and store the data into db_bookings
    #insert_1 (a tuple with same format in value of db_bookings), add it into db_bookings
    if stay_result == False:
        print ("your booking is failed due to potential existing bookig conflict, please re-book by adjusting your choice. ")
    else:
        insert_1 = (entered_site, entered_id, entered_occu)
        for i in list_1:
            if i not in db_bookings.keys():
                db_bookings[i] = insert_1
            else:
                db_bookings[i].insert(len(db_bookings[i]),insert_1[:])

        print(db_bookings)
        print("congratulation, you've booked successfully! ")
            
    input("\nPress Enter to continue.")

# function to display the menu
def disp_menu():
    print("==== WELCOME TO SELWYN CAMPGROUND ===")
    print(" 1 - List Customers")
    print(" 2 - List Campsites")
    print(" 3 - List Campers (Specific Date)")
    print(" 4 - Add Customer")
    print(" 5 - Add Booking")
    print(" X - eXit (stops the program)")


# ------------ This is the main program ------------------------

# Display menu for the first time, and ask for response
disp_menu()
response = input("Please enter menu choice: ")

# Don't change the menu numbering or function names in this menu
# Repeat this loop until the user enters an "X"
if response == "1":
    list_customers()
elif response == "2":
    list_campsites()
elif response == "3":
    list_campers_by_date()
elif response == "4":
    add_customer()
elif response == "5":
    add_booking()
elif response == "X" or response == "x":
    exit()
else:
    print("\n***Invalid response, please try again (enter 1-5 or X)")

print("")
disp_menu()
response = input("Please select menu choice: ")

print("\n=== Thank you for using Selywn Campground Administration! ===\n")
