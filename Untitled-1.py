
# response = input("sss")

# if response == "1":
#     print("1")
# elif response == "2":
#     print("2")
# elif response == "3":
#     print("3")
# elif response == "4":
#     print("4")
# elif response == "5":
#     print("5")
# elif response == "X" or response == "x":
#     exit()
# else:
#     print("\n***Invalid response, please try again (enter 1-5 or X)")


import camp_data
import datetime


col_customers = camp_data.col_customers
db_customers = camp_data.db_customers
col_bookings = camp_data.col_bookings
db_bookings = camp_data.db_bookings
UNPS = camp_data.UNPS #list of unpowered sites
PS = camp_data.PS #list of powered sites
# db1_customer = camp_data.db_customers

# def next_no(dicc):
#     return max(dicc.keys())+1

# def add_custmer():
#     new_name = str(input("please enter a new name: "))
#     new_email = str(input("please enter a new email: "))
#     new_phone = str(input("please enter a new phone number: "))
#     new_l = {'name':new_name, 'email': new_email, 'phone': new_phone}
#     db1_customer[next_no(db1_customer)] = new_l
#     last_key = list(db1_customer)[-1]


# add_custmer()
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




# def list_campsites():
#     # List the ID, name, occupancy
    
#     #merge UNPS and PS for sorting
#     unordered_list = []
#     unordered_list.extend(PS)
#     unordered_list.extend(UNPS)
#     ordered_list = sorted(unordered_list, key = lambda x: (x[0], x[1]))

#     # #create column dictionary to display campsites
#     col_PS = {'site identifier':str, 'maximum occupancy':int}
#     format_list_campsites = "{:.<3} | {:.^1} "
#     column_output(ordered_list, col_PS, format_list_campsites)

#     input("\nPress Enter to continue.")

# list_campsites()
        
# def add_booking():
#     # Add a booking
#     # Remember to validate customer ids and sites

#     #check if the customer name already registered in system
#     entered_name = str(input("Please enter your name: "))
#     result = any(entered_name in d.values() for d in db_customers.values())
#     if result == False:
#         print("Please register before you continue to booking. ")

#     #ask customer to enter the date of check-in
#     entered_year = int(input("Please enter the year: "))
#     entered_month = int(input("Please enter the month: "))
#     entered_day = int(input("Please enter the day: "))
#     entered_date = datetime.date(entered_year,entered_month,entered_day)
#     if entered_date < datetime.date.today():
#         print("Please re-enter a valid date. ")
    
#     #get the number of nights
#     stay_nights = int(input("Please enter days you want to stay: (5 days max) "))
#     if stay_nights > 5:
#         print("The days you entered has overed the max, please re-enter a valid number: ")
    
#     #get and check the user input is in the range of valid sites
#     entered_site = input("Please choose a site from U01-U09 or P01-P13: ")
    
#     l1 = []
#     l2 = []
#     for x in range(0,13):
#         l1.append(PS[x][0])
#     for y in range(0,9):
#         l2.append(UNPS[y][0])

#     if entered_site not in l1 and entered_site not in l2:
#         print("Please enter a valid site: ")

#     #check the selected site first, if not booed ever, directly add booking information into list
#     result_site = any(entered_site in d.list() for d in db_customers.values())
#     print(result_site)
                



# add_booking()

#verify if the user exists by checking id and name
def isAccountExist(your_id, your_name):
    account_result = False
    result_id_exist = any(your_id for d in db_customers.keys())
    result_name_exist = any(your_name in d.values() for d in db_customers.values())
    if result_id_exist == True and result_name_exist == True:
        account_result = True
        return account_result
    else:
        print("Please register before you continue booking. ")

#check availability in the selected site at selected date
def isAvailable(your_site, your_date, your_occu):
    #merge campsites list to check occupant later
    camp_list = []
    camp_list.extend(PS)
    camp_list.extend(UNPS)

    #check if the user selected date has been scheduled
    #if the date have no previous booking, then check selected occupancy
    if your_date not in db_bookings.keys():
        for i in range(len(camp_list)):
            if camp_list[i][0] == your_site:
                result_occu1 = (camp_list[i][1] - your_occu) >= 0
                return result_occu1
        
    #selected date got booking information
    #check if selected site got booked
    else:
        result_site_check = any(your_site in x[0] for x in db_bookings[your_date])
    #your selected site at selected date has been booked
        if result_site_check == True:
            return False
    #check occupants
        else:
            for i in range(len(camp_list)):
                if camp_list[i][0] == your_site:
                    result_occu2 = (camp_list[i][1] - your_occu) >= 0
                    return result_occu2
    
    
def add_booking():
    #get user name and id
    entered_name = input("Please enter your name: ")
    entered_id = input("Please enter your id: ")

    if isAccountExist(entered_id, entered_name) == False:
        print("Please input correct name and id: ")
    else:
    #get user check-in date
        entered_year = int(input("Please enter the year: "))
        entered_month = int(input("Please enter the month: "))
        entered_day = int(input("Please enter the day: "))
        entered_date = datetime.date(entered_year,entered_month,entered_day)
        if entered_date < datetime.date.today():
            print("Please re-enter a valid date. ")
    
    #get user site and check the input validity
        entered_site = input("Please choose a site from U01-U09 or P01-P13: ")

        l1 = []
        l2 = []
        for x in range(0,13):
            l1.append(PS[x][0])
        for y in range(0,9):
            l2.append(UNPS[y][0])

        if entered_site not in l1 and entered_site not in l2:
            print("Please enter a valid site: ")

    #get user occu and stays
        entered_occu = int(input("Please enter your occupants: "))
        entered_stay = int(input("Please enter days you want to stay: (5 days max) "))
        if entered_stay> 5 or entered_stay < 1:
            print("The days you entered is incorrect, please re-enter a valid number: ")
    
    #check every of your staying day availability
        list_1 = []
        list_2 = []
        list_3 = []
        for i in range(0, entered_stay):
            list_1.append(entered_date + datetime.timedelta(days = i))
            new_l = (int(list_1[i].strftime("%Y")), int(list_1[i].strftime("%m")), int(list_1[i].strftime("%d")))
            list_3.append(new_l)
            list_2.append(isAvailable(entered_site, datetime.date(*new_l), entered_occu))
        stay_result = False not in list_2

        if stay_result == False:
            return ("your booking is failed due to existing bookig conflict, please re-enter your choice: ")
        else:
    #add booking and store data into db_bookings
            insert_1 = (entered_site, entered_id, entered_occu)
            for i in list_3:
                if i not in db_bookings.keys():
                    db_bookings[datetime.date(*i)] = insert_1
                else:
                    db_bookings[i].insert(len(db_bookings[i]),insert_1[:])
                    print(db_bookings)
            print("congratulation, you've booked successfully! ")

add_booking()