income = int(input("enter your encome :"))
taxe_payable = 0
print("given encome ",income)
if income <= 10000:
    taxe_payable = 0
elif income<= 20000:
    #no tax on first 10k 
    x = income - 10000
    taxe_payable = x*10/100
else:
    taxe_payable = 0
    #next 10000 10% tax 
    taxe_payable = 10000*10/100
    # remaining 20% tax 
    taxe_payable += (income - 20000)*20/100
print("total payable tax is ",taxe_payable )

