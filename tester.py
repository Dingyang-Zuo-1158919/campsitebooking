import camp_data    # camp_data.py MUST be in the SAME FOLDER as this file!
import datetime     # We are using date times for this assessment, and it is
import re

col_customers = camp_data.col_customers
db_customers = camp_data.db_customers
col_bookings = camp_data.col_bookings
db_bookings = camp_data.db_bookings
UNPS = camp_data.UNPS #list of unpowered sites
PS = camp_data.PS #list of powered sites


def insert_to_db_booking(your_site, your_id, your_occu):
    entered_date = datetime.date(2024,4,11)
    entered_stay = 6
    
    list_1 = []
    for i in range(0, entered_stay):
        list_1.append(entered_date + datetime.timedelta(days = i))

    insert_1 = (your_site, your_id, your_occu)

    list_UNPS_name = []
    for x in range(len(UNPS)):
        list_UNPS_name.append(UNPS[x][0])
    list_PS_name = []
    for y in range(len(PS)):
        list_PS_name.append(PS[y][0])

    for i in list_1:
        if i not in db_bookings.keys():
            db_bookings[i] = [insert_1]
        else:
            if db_bookings[i][0][0][0] in list_UNPS_name:
                if your_site in list_UNPS_name:
                    db_bookings[i][0].append(insert_1)
                    db_bookings[i][0].sort(key = lambda x: x[0][0])
                else:
                    db_bookings[i][1].append(insert_1)
                    db_bookings[i][1].sort(key = lambda x: x[0][0])
            else:
                db_bookings[i][0][0][0] in list_PS_name
                if your_site in list_UNPS_name:
                    db_bookings[i].insert(0,[insert_1])
                    sorted(db_bookings[i][0], key = lambda x: x[0][0])
                else:
                    db_bookings[i][0].append(insert_1)
                    sorted(db_bookings[i][0], key = lambda x: x[0][0])
    updated_db_bookings = sorted(db_bookings.items(),key = lambda x: x[0])
    # db_bookings = updated_db_bookings
    print(f'Congratulation! Your booking is successful, Below is your booking information, \n name: {}, check-in date: {entered_date},  ')


insert_to_db_booking("U03",1659,2)