#This is my fisrt ptyhon project I hope you like it
print("Welcome to chebbi's restaurant")

import time
time.sleep(1)

name = input("What's your name ?\n")

import time
time.sleep(2)

if name == "Ben" or name == "Mohammed" or name == "Said" :
    Evil_State = input("Are you Evil " + name + "?\n")
    gooddeeds = int(input("how many gooddeeds did you do taday?"))
    if Evil_State == "Yes" and gooddeeds < 4:
        print("You are not welcome here \nGet out!!!!!!!!!!")
        import time
        time.sleep(2)
        exit()
    else:
        print("Don't worry i will not kick you\n")
      
else:
    print("Hello " + name + " how can I help you today ? ")


#menu
menu = "Coffee , Donut , Coffee with Milk."
#price
price = 10


print("here is the menu " + name + "\n" + menu )

import time
time.sleep(2)

print("ok " + name + " what do you want to order? \n" )

order = input() 
if order == "Coffee":
    print("we have Coffee")
elif order == "Coffee with Milk":
    print("we have Coffee with Milk")
elif order == "Donut":
    print("we have Donut ")
else:  
    print("Sorry we don't have that here")
    exit()
    
if order == "Coffee":
    price = 5
elif order == "Donut":
    price = 2
elif order == "Coffee with Milk":
    price = 10

many = input("how many " + order + " you want " + name + " ? \n")

total = price * int(many)

import time
time.sleep(2) 


print("sounds good " + name + " we will make your " + many + " " + order + " ready for you" ) 

import time
time.sleep(4)

print("ok " + name + " the " + many + "  " + order + " is ready !" ) 

import time
time.sleep(1)

print("the total is: $" + str(total))

pay = input("pay cash because we dont have visa " + name +"\n") 

if pay == str(total):
    print("Come back again !!")
else:
    print("U still didn't pay full cash sir")    

import time
time.sleep(2)
exit()


