##input we need from the users 
# total rent
#total food ordered for snacking
#electricity units spend
#charge per unit

##output 
#total uh ve to pay
def rent():
    total_frnds=int(input("enter the no. of person living in a room:"))
    total_rent=int(input("enter total rent:"))
    total_food=int(input("Enter for total food spending:"))
    electricity=int(input("enter the electricity spend:"))
    charge_per_unit=int(input("enter charge per unit unit:"))
    total_bill=electricity*charge_per_unit
    rent=(total_food+total_rent+total_bill)/total_frnds
    
    print("your part of amount is: ", rent)  
rent()   


