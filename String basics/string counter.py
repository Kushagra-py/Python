#to find types of chr and number of them
string = input('Enter string: ')
up=0
low=0
dig=0
spl=0
for i in string:
    if i.isupper():
        up+=1
    elif i.islower():
        low+=1
    elif i.isdigit():
        dig+=1
    else:
        spl+=1
print(f" Upper case: {up}\n lower case: {low}\n digits: {dig}\n special chr: {spl}")      

slength = len(string)
print('Total number of chr in string: ',slength)

#to reverse the chr case
print("Reverse case of string is: ", end='')
for i in string:
    if i.isupper():
        print(i.lower(),end='')
    elif i.islower:
        print(i.upper(),end='')
    else:
        print(i,end='')
    
    
