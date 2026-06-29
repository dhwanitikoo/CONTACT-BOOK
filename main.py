print("===============CONTACT BOOK=================")
import json
f=open("PHONE_BOOK\contacts.json","r")
data=json.load(f)
f.close()
def ADD_DATA():
    count=int(input("HOW MANY CONTACTS YOU WANT TO ADD : "))
    for i in range(count):
        new_data={}
        name=input("ENTER NAME : ")
        number=int(input("ENTER NUMBER :"))
        new_data["NAME"]=name.upper()
        new_data["NUMBER"]=number
        data.append(new_data)
        print("CONTACT ADDED !")                         
    f=open("PHONE_BOOK\contacts.json","w")
    DATA=json.dump(data,f)
    f.close()
        
def show_all_contacts():
    f=open("PHONE_BOOK\contacts.json","r")
    toread=json.load(f)
    f.close()
    for i in toread:
        print("NAME : ",{i['NAME']})
        print("NUMBER :",{i['NUMBER']})
        print("-" * 30)

def to_delete():
    name_delete=input("NAME YOU WANT TO DELETE: ").upper()
    for i in data:
        if i["NAME"]==name_delete:
            data.remove(i)
            f=open("PHONE_BOOK\contacts.json","w")
            json.dump(data,f)
            f.close()
            print("CONTACT DELETED FOR",name_delete)
            break
    else:
        print("CONTACT NOT FOUND")

def search_by_name(a):
    for i in data:
        if i["NAME"]==a:
            print("NUMBER : ",i["NUMBER"])
            break
    else:
            print("RECORD NOT FOUND")
    
def search_by_number(a):
    for i in data:
        if i["NUMBER"]==a:
            print("NAME : ",i["NAME"])
            break
    else:
        print("RECORD NOT FOUND")
def edit(s):
    for i in data:
        if i["NAME"]==s:
            print("Contact Found !")
            print("1.Edit Name")
            print("2.Edit Number")
            print("3.Edit Both")
            editing(to_edit)
    
def editing(s):
    choice2=int(input("ENTER CHOICE : "))
    if choice2  not in (1,2,3):
        print("INVALID CHOICE") 
    
    for i in data:
        if i["NAME"]==s:
            if choice2==1 or choice2==3:
                print("Current Name : ",s)
                new_name=input("New Name : ").upper()
                i["NAME"]=new_name    
                print("NAME EDITED !")
            if choice2==2 or choice2==3:
                    print("Current Number : ",i["NUMBER"])
                    new_number=int(input("New Number : "))
                    i["NUMBER"]=new_number
                    print("NUMBER EDITED !")

            f=open("PHONE_BOOK\contacts.json","w")
            json.dump(data,f)
            f.close()
            
            return
    print("RECORD NOT FOUND")
        
        
print("1.ADD CONTACT")
print("2.SHOW ALL CONTACTS")
print("3.DELETE CONTACT")
print("4.SEARCH CONTACT")
print("5.TO EDIT")
choice=int(input("ENTER NUMBER : "))
if choice==1:
    ADD_DATA()
elif choice==2:
    show_all_contacts()
elif choice==3:
    to_delete()
elif choice==4:
    search_by=input("SEARCH : ")
    if search_by.replace(" ","").isalpha():
        search_by_name(search_by)
    elif search_by.isdigit():
        search_by_number(search_by)
elif choice==5:
    to_edit=input("ENTER CONTACT TO EDIT :").upper()
    edit(to_edit)
else:
    print("INVALID CHOICE")