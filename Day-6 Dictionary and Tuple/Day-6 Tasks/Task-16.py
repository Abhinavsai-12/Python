name="abhi"
password="123"
user_name=input("Enter the User Name:")
passwords=input("Enter the Password:")

operations='''
    1.Credit
    2.Debit
    3.Check Balance
    4.exit
'''


Amount=1000
if name==user_name and passwords==password:
    while True:
        print(operations)
        option=int(input("Enter the Option:"))


        if option==1:
            credit_amount=float(input("Enter the Amount:"))
            Amount+=credit_amount
            print("Amount after credit:",Amount)


        elif option==2:
            debit_amount=float(input("Enter the Amount:"))
            Amount-=debit_amount
            print("Amount after debit:",Amount)


        elif option==3:
            print("Balance Amount:",Amount)

            
        elif option==4:
            break

else:
    print("incorrect")


