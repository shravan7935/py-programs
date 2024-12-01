quantity = 3
totalMoney = 1000
price = 450 
# print("i have ",totalMoney, "dollars so i can buy", quantity," football for ",price,"dollars")
statement1 = "i have {1} dollars so i can buy {0} football for {2} dollars "
print(statement1.format(quantity,totalMoney,price))