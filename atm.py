import time

print("Please Insert Your CARD")

#for card processing
time.sleep(5)

password = 1228

#taking atm pin from user
pin = int(input("enter your atm pin "))

#user account balance
balance = 5000

#checking pin is valid or not 
if pin == password:
    #loop will run user get free 
    while True:

        #Showing  info to user

        print(""" 
			1 == Balance
			2 == Withdraw 
			3 == Deposit 
			4 == Exit
			"""
              )

        try:    
             #taking an option from user
            option = int(input("Please enter your choice "))
        except:
            print("Please enter valid option")
        
        #for option 1        
        if option == 1:
            print(f"Your current balance is {balance}")
                                     
        if option == 2:

            withdraw_amount = int(input("please enter withdraw_amount "))

            

            balance = balance - withdraw_amount

            print(f"{withdraw_amount} is debited from your account")

            

            print(f"your updated balance is {balance}")

            

        if option == 3:

            deposit_amount = int(input("please enter deposit_amount"))

            balance = balance + deposit_amount

            

            print(f"{deposit_amount} is credited to your account")



            print(f"your updated balance is {balance}")



        if option == 4:

            break


else:
    print("wrong pin Please try again")

