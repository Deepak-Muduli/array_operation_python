Name=[]
Phone_no=[]
Email_id=[]
Address=[]
num=int(input('enter how many address you want to given...'))
for i in range(num):
    name=input('enter name...')
    phone_no=int(input('enter the mobile number...'))
    mail=input('enter the mail...')
    address=input('enter the address...')
    
    Name.append(name)
    Phone_no.append(phone_no)
    Email_id.append(mail)
    Address.append(address)

print('THE ENTIRE DETAILS..')
for i in range(num):
    print(f"name is:{Name[i]} \n phone number is:{Phone_no[i]} \n email id is:{Email_id[i]} \n address is:{Address[i]}")  


print('are you want to update or delete the information')
update=input('are you want to update details yes or no')
while True:
    if update.lower()== 'yes':
        num=num+1
        name=input('enter name...')
        phone_no=int(input('enter the mobile number...'))
        mail=input('enter the mail...')
        address=input('enter the address...')
    
        Name.append(name)
        Phone_no.append(phone_no)
        Email_id.append(mail)
        Address.append(address)
        update1=input('are you want to update again yes or no')
        if update1.lower()!='yes':
            break 
print('the update address is...')
for i in range(num):
    print(f"name is:{Name[i]} \n phone number is:{Phone_no[i]} \n email id is:{Email_id[i]} \n address is:{Address[i]}") 

print('for delete address')
delete=input('are you want to delete yes or no')
while True:
    if delete.lower()=='yes':
        num=num-1
        del_con=input('enter the name you want delete')
        index=Name.index(del_con)
        Name.remove(Name[index])
        Phone_no.remove(Phone_no[index])
        Email_id.remove(Email_id[index])
        Address.remove(Address[index])
        del1=input('are you want to delete other cotact yes or no!')
        if del1.lower()!='yes':
            break

print("the delete update is ")
for i in range(num):
    print(f"name is:{Name[i]} \n phone number is:{Phone_no[i]} \n email id is:{Email_id[i]} \n address is:{Address[i]}")             

