pin=int(input("enter your pin number:"))
balance=10000
if(pin==1770):
    print("your pin was correct")
    menu=input("withdraw/deposit/check balance:")
    if(menu=="withdraw"):
       withdraw=int(input("enter your withdraw ammount:"))
       if(withdraw<=balance):
           if(withdraw>0):
              balance=(balance-withdraw)
              print("balance:",balance)
              print("sucessfully your amount was widhdrawed collecy your cash")
           else:
               print("invalid amount")
       elif(withdraw>balance):
           print("insufficient balance")
    elif(menu=="check balance"):
       print("your balance amount:",balance)
    elif(menu=="deposit"):
        deposit=int(input("enter you deposit amount:"))
        balance=(balance+deposit)
        print(balance)
        print("your amount was successfully debited")
    else:
        print("unvalid menu choose correct opition")
else:
    print("pin was wrong")
    
         
