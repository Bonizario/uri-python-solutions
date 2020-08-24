# 1134 - Type of Fuel
fuel = ""
alcohol = 0
gasoline = 0
diesel = 0
while fuel != "4":
    fuel = input()
    if (fuel != "1") and (fuel != "2") and (fuel != "3") and (fuel != "4"):
        fuel = input()
    if (fuel == "1"):
        alcohol += 1
    elif (fuel == "2"):
        gasoline += 1
    elif (fuel == "3"):
        diesel += 1
print("MUITO OBRIGADO")
print("Alcool: {}".format(alcohol))
print("Gasolina: {}".format(gasoline))
print("Diesel: {}".format(diesel))
