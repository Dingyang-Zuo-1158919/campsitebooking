# ============== SELEYN CAMPGROUND DATA ==============
# Student Name: Dingyang Zuo
# Student ID : 1158919
# ===============================================================================
 
import datetime

col_customers = {'ID':int,'Name':str,'Telephone':str,'e-mail':str}
db_customers = {563:{'name':'Simon Smith','phone':'0244881901','email':'simon@smith.nz'},241:{'name':'Jasmine Holiday','phone':'0274823801','email':'jaz@onholiday.co.nz'},1654:{'name':"Jonty Jensen",'email':"Jonty_Jensen@gmail.com",'phone':"(04) 120-8776"},
1655:{'name':"Kate McArthur",'email':"K_McArthur94@gmail.com",'phone':"(028) 195-3665"},
1656:{'name':"Jack Hopere",'email':"Jack643@gmail.com",'phone':"(022) 497-2003"},
1657:{'name':"Chloe Mathewson",'email':"Chloe572@gmail.com",'phone':"(023) 662-1370"},
1658:{'name':"Kate McLeod",'email':"KMcLeod112@gmail.com",'phone':"(027) 557-8364"},
1659:{'name':"Sam Dawson",'email':"SamDawson@gmail.com",'phone':"(07) 172-1045"},
1660:{'name':"Heidi Delaney",'email':"HDelaney@gmail.com",'phone':"(028) 294-2819"},
1661:{'name':"Michael Wright",'email':"Michael_Wright@gmail.com",'phone':"(03) 751-2653"},
1662:{'name':"Elizabeth Preston",'email':"ElizabethPreston@gmail.com",'phone':"(09) 425-5377"}}
col_bookings = {'Date':datetime.date,'Name':str,'Occupants':int}
db_bookings = {datetime.date(2024,4,11):[[('U01',563,1)],[('P04',1655,3),('P07',241,2)]],datetime.date(2024,4,12):[[('U01',563,1)],[('P04',1655,3),('P07',241,2)]],datetime.date(2024,4,13):[[('U01',563,1)],[('P04',1655,3),('P11',1661,2)]],datetime.date(2024,4,15):[[('U07',1659,5)]]}
UNPS = [('U01',2),('U02',5),('U03',4),('U04',4),('U05',4),('U06',2),('U07',6),('U08',4),('U09',8)]
PS = [('P01',2),('P02',2),('P03',4),('P04',6),('P05',6),('P06',6),('P07',6),('P08',6),('P09',4),('P10',4),('P11',2),('P12',6),('P13',6)]
