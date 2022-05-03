#Program: Commissions
#Author: Danique Dalmage
#Date Created: April 30, 2022
#Course: ITT103
#Purpose: This program is created to accept the sales person number, sales amount and class of an undetermined amount of
#salespersons then calculate the commissions earned. 

run = True
#while run is true, the code will execute repeatedly (accepting an unspecified amount of inputs)until the user enters a value that makes run false

while run == True:
 salesperson_num = int(input("Enter the sales number of the sales person "))
 #user being prompted to enter sales number.
 sales_amt = float(input("Enter the sales amount "))
 #user being prompted to enter sales amount.
 sales_class = input("Enter the sales class ")
 #user being prompted to enter sales class.

 if sales_class == "1":
   #Checking if the class is 1 and assigning the commission rates based on the amount of sales.
    if sales_amt <= 1000.00:
      comm_rate = 0.06
    elif sales_amt >1000.00 and sales_amt <2000.00:
      comm_rate = 0.07
    else:
      comm_rate = 0.1

 
 #Checking if the class is 2 and assigning the commission rates based on the amount of sales.
 elif sales_class == "2":
   if sales_amt < 1000.00:
      comm_rate = 0.04
   else:
     comm_rate = 0.06
   
 #Checking if the class is 3 and assigning the commission rate.
 elif sales_class == "3":
      comm_rate = 0.045
      
 #If the class is not from one to three, an error code will be printed. 
 else:
     print("Please enter a valid class")
     comm_rate = 0
       
    
#commmissions is being calculated and formatted to be 2 decimal places
 if comm_rate != 0:
  comm = sales_amt * comm_rate
  print(f"The commission for the sales person", salesperson_num, "is $", format(comm ,',.2f'))

#Checking if the user wants to end the program. If yes, they are prompted to enter 'exit'.
 exit=input("Input *exit* (case sensitive) to end the program, or any other key to continue ")
 if exit == "exit":
  run == False
  break




 
 
