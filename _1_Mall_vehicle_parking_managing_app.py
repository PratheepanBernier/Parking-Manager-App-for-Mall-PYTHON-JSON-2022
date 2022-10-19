import json
import re
from json import JSONDecodeError
from datetime import datetime,date

def login(type):
    type1=type
    if type1=="admin":
        print("\n---Administrator Login---")
    if type1=="manager":
        print("\n---Parking Manager Login---")
    flag=0
    while flag==0:
        emp_id = input("\nEnter your Employee ID : ")
        emp_id_pattern = "[0-9]{5}"
        if emp_id=="" :
            print("Employee ID cannot be Empty !")

        elif re.findall(emp_id_pattern,emp_id)==[] and not emp_id=="":
            print("Employee ID must contain only numbers and can be of only 5 digits !")
        
        elif len(emp_id)>5:
            print("Employee ID cannot exceed more than 5 digits!")
        else :
            flag=1
            employee_id=emp_id

    flag_=0
    while flag_==0:
        password = input("\nEnter your Password : ")
        password_pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$!*%^&+=]).*$"
        if password=="":
            print("Password cannont be left empty !")
        elif re.findall(password_pattern,password) == [] and not password=="" :
            print("Password must contain atleast 8 characters with altleast 1 upper case letter, 1 lower case letter and 1 special characters !")
        else :
            flag_=1
    
    d=0
    if type=='admin':
        f=open('_2_admin_login_credentials.json','r+')
    if type=="manager":
        f=open('_3_parking_manager_details.json','r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        return False
    for i in range(len(content)):
        if content[i]["Employee ID"]==employee_id and content[i]["Password"]==password:
            d=1
            print("\nLogged in Successfully !!! \n---")
                
    if d==1:
        f.close()
        return True
    if d==0:
        print("\nIncorrect login credentials ! \n---")
        f.close()
        return False

def add_new_parking_manager():

    print("---New Parking Manager Registration---")

    def manager_name():
        flag=0
        while flag==0:
            name = input("Enter new Parking manager's Name : ")
            name_pattern = "[a-zA-Z]{1,}"
            if name=="" and not re.findall(name_pattern,name) == []:
                print("Name cannot be Empty !")
            elif re.findall(name_pattern,name) == [] and not name=="":
                print("Name can contain only Alphabets !")
            else:
                flag=1
        return name

    def manager_employee_id():
        flag=0
        while flag==0:
            employee_id = input("Enter new Parking manager's Employee ID : ")
            employee_id_pattern = "[0-9]{5}"
            if employee_id=="" and not re.findall(employee_id_pattern,employee_id)==[]:
                print("Employee ID cannot be Empty !")

            elif re.findall(employee_id_pattern,employee_id)==[] and not employee_id=="":
                print("Employee ID can contain only numbers and can be of only 5 digits !")
            
            else:
                flag=1
        return employee_id

    def manager_mobile_number():
        flag=0
        while flag==0:
            mobile_number = input("Enter new Parking manager's Mobile Number : ")
            mobile_number_pattern="^[0-9]{10}"
            if mobile_number=="" and not re.findall(mobile_number_pattern,mobile_number)==[]:
                print("Mobile Number cannot be Empty !")
            
            elif re.findall(mobile_number_pattern,mobile_number)==[] and not mobile_number=="":
                print("Mobile number can contain only numbers and can be of only 10 digits !")
            
            else:
                flag=1
        return mobile_number

    def manager_password():
        flag=0
        while flag==0:
            password = input("Enter password that you wish to assign for him/her : ")
            password_pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
            if password=="" and not re.findall(password_pattern,password) == []:
                print("Password cannont be left empty !")
            elif re.findall(password_pattern,password) == [] and not password=="" :
                print("Password must contain atleast 8 characters with altleast 1 upper case letter, 1 lower case letter and 1 special characters !")
            else:
                flag=1
        return password

    name = manager_name()
    emp_id = manager_employee_id()
    mob_no = manager_mobile_number()
    pass_word = manager_password()

    f=open('_3_parking_manager_details.json','r+')
    d={
        "Full Name":name,
        "Employee ID":emp_id,
        "Mobile Number":mob_no,
        "Password":pass_word
    }
    
    try:
        content=json.load(f)
        if d not in content:
            content.append(d)
            f.seek(0)
            f.truncate()
            json.dump(content,f)
            f.close()
        return True
    except JSONDecodeError:
        l=[]
        l.append(d)
        json.dump(l,f)
        f.close()
        return True
    
    
def view_parked_vehicles_list():
    d=0
    f=open('_4_vehicle_details.json','r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        print("List is Nil! \n---")
        f.close()
        return False
    
    for i in range(len(content)-1,-1,-1):
        d=1
        token_number = i+1
        print(f"Bike token number : {token_number}")
        for k,v in content[i].items():
            if v!="Nil":
                print(f"{k} : {v}")
    
    if d==1:
        f.close()
        return True

    if d==0:
        print("List is Nil! \n---")
        f.close()
        return False

def view_locked_vehicles_list():
    d=0
    f=open('_4_vehicle_details.json','r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        print("List is Nil! \n---")
        return False
    for i in range(len(content)-1,-1,-1):
        today = date.today()
        current_date = today.strftime("%d/%m/%Y")
        count1=0
        if content[i]["Parked Date"] != current_date and content[i]["Unparked Date"]=="Not yet":
            count1=count1+1
    
        if count1!=0:
            if content[i]["Parked Date"] != current_date and content[i]["Unparked Date"]=="Not yet":
                content[i]["Unparked Date"] = "LOCKED"
                content[i]["Unparked Time"] = "LOCKED"
                f.seek(0) 
                json.dump(content,f)
                f.truncate()

        count2=0
        if content[i]["Parked Date"] != current_date and content[i]["Unparked Date"]=="LOCKED":
            count2=count2+1
    
        if count2!=0:
            if content[i]["Parked Date"] != current_date and content[i]["Unparked Date"]=="LOCKED":
                d=1
                token_number = i+1
                print(f"Vehicle token number : {token_number}")
                for k,v in content[i].items():
                    if v!="Nil":
                        print(f"{k} : {v}")
            else:
                print("List is Nil")
        
    if d==1:
        f.close()
        print("Above vehicles are locked as they have been in the parking for more than one day. \nKindly ask the vehicle holder(s) to contact the admin to unlock the vehicles")
        return True

    if d==0:
        f.close()
        return False

def vehicle_unlock():
    d=0
    flag=0
    while flag==0:
        vehicle_number = input("Enter Vehicle number that need to be unlocked (Enter in this format Eg.PY 01 CQ 9900): ")
        vehicle_number_pattern="^[A-Z]{2}\s[0-9]{2}\s[A-Z]{2}\s[0-9]{4}$"
        if vehicle_number=="" and not re.findall(vehicle_number_pattern,vehicle_number)==[]:
            print("Vehicle Number cannot be Empty !")

        elif re.findall(vehicle_number_pattern,vehicle_number)==[] and not vehicle_number=="":
            print("Vehicle number should be in this Format eg. PY 01 CQ 9900 ")

        else:
            flag=1
            vehicle_num=vehicle_number
    
    flag1=0
    while flag1==0:      
        reason_for_not_unparked=input("Ask vehicle holder and Enter reason for not unparked : ")
        reason_pattern =""
        if reason_for_not_unparked==reason_pattern:
            print("Reason cannot be left empty! \n---")
        else:
            flag1=1
            reason_unpark = reason_for_not_unparked

    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    dt_string = now.strftime("%H:%M:%S")
    f=open('_4_vehicle_details.json','r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        print("No vehicle available to unlock\n---")
        return False
    for i in range(len(content)):
        if content[i]["Unparked Date"]!="LOCKED" and content[i]["Vehicle Number"]==vehicle_num and content[i]["Remark"]!="Handed over to Police" :
            print("This vehicle is not locked! \n---")

    for i in range(len(content)):
        if content[i]["Unparked Date"]=="LOCKED" and content[i]["Vehicle Number"]==vehicle_num:
            content[i]["Unparked Date"] = current_date
            content[i]["Unparked Time"] = dt_string
            content[i]["Remark"] = "UNLOCKED"
            content[i]["Reason for Not Unparked"] = reason_unpark

            d=1
            temp=i
            park_date_=content[temp]["Parked Date"]
            unpark_date=content[temp]["Unparked Date"]
            d1 = datetime.strptime(park_date_, "%d/%m/%Y")
            d2 = datetime.strptime(unpark_date, "%d/%m/%Y")
            date_difference=d2-d1
            date_diff = date_difference.days
            if date_diff>10 :
                print("Since your bike has been parked for more than 10 days, it has been handed over to nearby police station. \nKindly contact nearby police station")
                content[i]["Unparked Date"] = "Handed over to Police"
                content[i]["Unparked Time"] = "Handed over to Police"
                content[i]["Remark"] = "Handed over to Police"
                content[i]["Reason for Not Unparked"] = "Handed over to Police"
                d=2
            f.seek(0) 
            json.dump(content,f)
            f.truncate()
        
    if d==1:
        print("Unlocked successfully")
        bike_initial_price=150
        car_auto_initial_price=200
        bus_van_initial_price=250
        park_date_=content[temp]["Parked Date"]
        unpark_date=content[temp]["Unparked Date"]
        d1 = datetime.strptime(park_date_, "%d/%m/%Y")
        d2 = datetime.strptime(unpark_date, "%d/%m/%Y")
        date_difference=d2-d1
        date_diff = date_difference.days 

        if date_diff<=1:
            if content[temp]["Vehicle Type"]=="Bike":
                final_price = bike_initial_price
            if content[temp]["Vehicle Type"]=="Car" or content[temp]["Vehicle Type"]=="Auto":
                final_price = car_auto_initial_price
            if content[temp]["Vehicle Type"]=="Bus" or content[temp]["Vehicle Type"]=="Van":
                final_price = bus_van_initial_price
        else :
            calc1=date_diff-1
            if content[temp]["Vehicle Type"]=="Bike":
                final_price = bike_initial_price+calc1*150
            if content[temp]["Vehicle Type"]=="Car" or content[temp]["Vehicle Type"]=="Auto":
                final_price = car_auto_initial_price+calc1*200
            if content[temp]["Vehicle Type"]=="Bus" or content[temp]["Vehicle Type"]=="Van":
                final_price = bus_van_initial_price+calc1*250

        content[temp]["Price"]=final_price
        f.seek(0) 
        json.dump(content,f)
        f.truncate()

        f.close()
        print(f"Vehicle holder has to pay Rs.{final_price}")
        return True
    if d==2:
        f.close()
        return True
    if d==0:
        f.close()
        return False

def view_unlocked_vehicles_list():
    d=0
    f=open('_4_vehicle_details.json','r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        print("List is Nil! \n---")
        f.close()
        return False
    for i in range(len(content)):
        count=0
        if content[i]["Remark"]=="UNLOCKED" :
            count=count+1

        if count!=0:
            if content[i]["Remark"]=="UNLOCKED" :
                d=1
                token_number = i+1
                print(f"Vehicle token number : {token_number}")
                for k,v in content[i].items():
                    print(f"{k} : {v}")
        else:
            print("\nList is Nil! \n---")
        
    if d==1:
        print("\nAbove vehicles are unlocked!!! \n---")
        f.close()
        return True

    if d==0:
        f.close()
        return False


def add_new_vehicle_to_parking():

    def vehicle_owner_name():
        flag=0
        while flag==0:
            vehicle_holder_name = input("Enter Vehicle holder name : ")
            name_pattern = "[a-zA-Z]{1,}"
            if vehicle_holder_name=="" and not re.findall(name_pattern,vehicle_holder_name) == []:
                print("Name cannot be Empty !")
                
            if re.findall(name_pattern,vehicle_holder_name) == [] and not vehicle_holder_name == "":
                print("Name can contain only Alphabets !")
            
            if re.findall(name_pattern,vehicle_holder_name) != [] and vehicle_holder_name != "":
                flag=1
        return vehicle_holder_name

    def vehicle_owner_vehicle_no():
        flag=0
        while flag==0:
            vehicle_number = input("Enter Vehicle number (Enter in this format Eg.PY 01 CQ 9900): ")
            vehicle_number_pattern="^[A-Z]{2}\s[0-9]{2}\s[A-Z]{2}\s[0-9]{4}$"
            if vehicle_number=="" and not re.findall(vehicle_number_pattern,vehicle_number)==[]:
                print("Vehicle Number cannot be Empty !")

            if re.findall(vehicle_number_pattern,vehicle_number)==[] and not vehicle_number=="":
                print("Vehicle number should be in this Format eg. PY 01 CQ 9900 ")

            if re.findall(vehicle_number_pattern,vehicle_number) != [] and vehicle_number != "":
                flag=1
        return vehicle_number
        

    def vehicle_owner_mob_no():
        flag=0
        while flag==0:
            vehicle_holder_mobile_number = input("Enter Vehicle Holder's Mobile Number : ")
            mobile_number_pattern="^[0-9]{10}"
            if vehicle_holder_mobile_number=="" and not re.findall(mobile_number_pattern,vehicle_holder_mobile_number)==[]:
                print("Mobile Number cannot be Empty !")

            if re.findall(mobile_number_pattern,vehicle_holder_mobile_number)==[] and not vehicle_holder_mobile_number=="":
                print("Mobile number can contain only numbers and can be of only 10 digits !")

            if re.findall(mobile_number_pattern,vehicle_holder_mobile_number) != [] and vehicle_holder_mobile_number != "":
                flag=1
        return vehicle_holder_mobile_number

    def vehicle_type():
        
        flag=0
        while flag==0:
            choice3 = input("Vehicle Type :- \n1.Bike \n2.Auto \n3.Car \n4.Van \n5.Bus \nEnter your choice : ") 
            if choice3 == '1':
                vehicle_type1 = "Bike"
                flag=1
            elif choice3 == '2':
                vehicle_type1 = "Auto"
                flag=1
            elif choice3 == '3':
                vehicle_type1 = "Car"
                flag=1
            elif choice3 == '4':
                vehicle_type1 = "Van"
                flag=1
            elif choice3 == '5':
                vehicle_type1 = "Bus"
                flag=1
            else :
                print("Invalid input \nEnter values from 1 to 5")
            
        return vehicle_type1


    name = vehicle_owner_name()
    vehicle_no = vehicle_owner_vehicle_no()
    vehicle_model = vehicle_type()
    mob_no = vehicle_owner_mob_no()
    today = date.today()
    parked_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    dt_string = now.strftime("%H:%M:%S")
    parked_time = dt_string
    unpark_time = "Not yet"
    unpark_date = "Not yet"
    remark="Nil"
    reason="Nil"
    price="Nil"

    print("New vehicle added sucessfully !!!")

    temp=0

    f=open('_4_vehicle_details.json','r+')
    d={
        "Vehicle Holder Name":name,
        "Vehicle Number":vehicle_no,
        "Vehicle Type":vehicle_model,
        "Vehicle Holder Mobile Number":mob_no,
        "Parked Date":parked_date,
        "Parked Time":parked_time,
        "Unparked Time": unpark_time,
        "Unparked Date":unpark_date,
        "Remark":remark,
        "Reason for Not Unparked": reason,
        "Price":price

    }
    try:
        content=json.load(f)
        if d["Vehicle Number"] not in content:
            content.append(d)
            f.seek(0)
            f.truncate()
            json.dump(content,f)
            temp=1

        else:
            print("Vehicle already is in the parking. \nUnpark to re-park.")
            
    except JSONDecodeError:
        l=[]
        l.append(d)
        json.dump(l,f)
    if temp==1:
        f.close()
        return True
    else : 
        f.close()
        return False


def unpark_a_vehicle_from_parking():
    flag=0
    while flag==0:
        vehicle_number_=input("\nEnter a Vehicle number that need to be Unparked : ")
        vehicle_number_pattern="^[A-Z]{2}\s[0-9]{2}\s[A-Z]{2}\s[0-9]{4}$"
        if vehicle_number_=="" and not re.findall(vehicle_number_pattern,vehicle_number_)==[]:
            print("\nVehicle Number cannot be Empty !")

        elif re.findall(vehicle_number_pattern,vehicle_number_)==[] and not vehicle_number_=="":
            print("\nVehicle number should be in this Format eg. PY 01 CQ 9900 ")

        else:
            veh_number=vehicle_number_
            flag=1
        
    today = date.today()
    unparked_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    unparked_time = now.strftime("%H:%M:%S")
    d=0
    f=open('_4_vehicle_details.json','r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        print("No vehicle available for Unparking! \n---")
        return False
    for i in range(len(content)):
        if content[i]["Vehicle Number"]==veh_number and content[i]["Parked Date"]==unparked_date:
            d=1
            temp = i
            f.close()
            break

        if content[i]["Vehicle Number"]==veh_number and content[i]["Parked Date"]!=unparked_date:
            print("\nThe vehicle has been locked since it has been in the parking for more than one day. \nKindly redirect them to admin to unlock the vehicle. \n---")
            f=open('_4_vehicle_details.json','r+')
            try:
                content=json.load(f)
            except JSONDecodeError:
                f.close()
                return False
            content[i]["Unparked Date"] = "LOCKED"
            content[i]["Unparked Time"] = "LOCKED"
            f.seek(0) 
            json.dump(content,f)
            f.truncate()

        if content[len(content)-1]["Vehicle Number"]!=veh_number:
            print("\nNo such vehicle number exists in the list! \n---")

    
    if d==0:
        f.close()
        return False
    else:
        f=open('_4_vehicle_details.json','r+')
        try:
            content=json.load(f)
        except JSONDecodeError:
            f.close()
            return False
        bike_initial_price=20
        car_auto_initial_price=30
        bus_van_initial_price=50
        park_time_=content[temp]["Parked Time"]
        t1 = datetime.strptime(park_time_, "%H:%M:%S")
        t2 = datetime.strptime(unparked_time, "%H:%M:%S") 
        time_difference = t2-t1
        time_difference_in_sec = time_difference.total_seconds() 
        if time_difference_in_sec<=10800.0:
            if content[temp]["Vehicle Type"]=="Bike":
                final_price = bike_initial_price
            if content[temp]["Vehicle Type"]=="Car" or content[temp]["Vehicle Type"]=="Auto":
                final_price = car_auto_initial_price
            if content[temp]["Vehicle Type"]=="Bus" or content[temp]["Vehicle Type"]=="Van":
                final_price = bus_van_initial_price
        else :
            calc=time_difference_in_sec-10800.0
            calc1=calc//3600.0
            if content[temp]["Vehicle Type"]=="Bike":
                final_price = bike_initial_price+calc1*10
            if content[temp]["Vehicle Type"]=="Car" or content[temp]["Vehicle Type"]=="Auto":
                final_price = car_auto_initial_price+calc1*10
            if content[temp]["Vehicle Type"]=="Bus" or content[temp]["Vehicle Type"]=="Van":
                final_price = bus_van_initial_price+calc1*10
        content[temp]["Unparked Date"] = unparked_date
        content[temp]["Unparked Time"] = unparked_time
        content[temp]["Price"]=final_price
        f.seek(0) 
        json.dump(content,f)
        f.truncate()
        f.close()
        print(f"\nVehicle holder has to pay Rs.{final_price}")
        print("Unparking Done!!! \n---")
        return True

def vehicle_owner():
    flag=0
    while flag==0:
        veh_num = input("Enter your Vehicle number (Enter in this format Eg.PY 01 CQ 9900): ")
        vehicle_number_pattern="^[A-Z]{2}\s[0-9]{2}\s[A-Z]{2}\s[0-9]{4}$"

        if veh_num=="" and not re.findall(vehicle_number_pattern,veh_num)==[]:
            print("Vehicle Number cannot be Empty !")

        elif re.findall(vehicle_number_pattern,veh_num)==[] and not veh_num=="":
            print("Vehicle number should be in this Format eg. PY 01 CQ 9900 ")

        else :
            flag=1
            vehicle_number = veh_num
    
    flag1=0
    while flag1==0:
        mob_num = input("Enter new Parking manager's Mobile Number : ")
        mobile_number_pattern="^[0-9]{10}"

        if mob_num=="" and not re.findall(mobile_number_pattern,mob_num)==[]:
            print("Mobile Number cannot be Empty !")
            
        elif re.findall(mobile_number_pattern,mob_num)==[] and not mob_num=="":
            print("Mobile number can contain only numbers and can be of only 10 digits !")
            
        else:
            flag1=1
            mobile_number=mob_num
    d=0
    f=open('_4_vehicle_details.json','r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        print("No such vehicle exists! \n---")
        return False
    for i in range(len(content)-1,-1,-1):
        if content[i]["Vehicle Number"]==vehicle_number and content[i]["Vehicle Holder Mobile Number"]==mobile_number :
            d=1
            token_number = i+1
            print(f"Bike token number : {token_number}")
            for k,v in content[i].items():
                print(f"{k} : {v}")
    
    if d==1:
        f.close()
        return True

    if d==0:
        f.close()
        return False
    
def welcome():
    flag=0
    while flag==0:
        print("Welcome to XYZ Mall !!!")
        choice1 = input("Who are you? \n1.Administrator \n2.Parking manager \n3.Vehicle owner \n4.Exit from the app \n \nEnter your choice : ")
        if choice1=='1':
            if login("admin") == True:
                flag1=0
                while flag1==0:
                    print("1.Add new Parking Manager \n2.View list of vehicles parked and unparked \n3.View List of vehicles Locked \n4.Unlock a vehicle \n5.View list of Unlocked vehicles \n6.Logout")
                    choice2 = input("Enter your Choice : ") 
                    if choice2 == '1':
                        if add_new_parking_manager()==True:
                            print("New Parking Manager added Successfully!!! \n---")
                    elif choice2 == '2':
                        view_parked_vehicles_list()
                    elif choice2 == '3':
                        view_locked_vehicles_list()
                    elif choice2 == '4':
                        vehicle_unlock()
                    elif choice2 == '5':
                        view_unlocked_vehicles_list()
                    elif choice2 == '6':
                        flag1=1
                        exit()
                    else :
                        print("Invalid input \nEnter values from 1 to 6 \n---")


        elif choice1=='2':
            if login("manager") == True:
                flag2=0
                while flag2==0:
                    print("1.Add new vehicle to parking \n2.Unpark a vehicle \n3.Logout")
                    choice2 = input("Enter your Choice : ") 
                    if choice2 == '1':
                        add_new_vehicle_to_parking()
                    elif choice2 == '2':
                        unpark_a_vehicle_from_parking()
                    elif choice2 == '3':
                        flag2=1
                        exit()
                    else :
                        print("Invalid input \nEnter values from 1 to 4 \n---")


        elif choice1=='3':
            print("Enter your bike details :- ")
            if vehicle_owner()==True:
                print("Details displayed Successfully !!!\n---")
            else:
                print("Invalid details ! \n---")
        
        elif choice1=='4':
            flag=1
        
        else:
            print("Invalid input \nEnter numbers between 1 to 4 \n---")

welcome()
