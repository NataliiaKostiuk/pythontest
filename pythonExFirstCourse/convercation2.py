amount = 0
currency = input("Please enter the currency you wabt to convert:(Dollars, Euro, Yaun, Mexican Peso )")
if currency.capitalize() == "Dollars":
  pounds = float(input("Please enter the amount of pounds: "))
  amount = pounds * 0.99
  print("The amount of dollars is: ", amount)
elif currency.capitalize() == "Euro":
  pounds = float(input("Please enter the amount of pounds: "))
  amount = pounds * 1.14
  print("The amount of euros is: ", amount)
elif currency.capitalize() == "Mexican Peso":
  pounds = float(input("Please enter the amount of pounds: "))
  amount = pounds * 19.86
  print("The amount of Mexican Pesos  is: ", amount)
else:
  print("Please enter the valid currency!")