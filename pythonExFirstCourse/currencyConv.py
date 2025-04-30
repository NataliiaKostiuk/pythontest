currency = input("Please enter the currency you wabt to convert: Pounds or Euro")
if currency.capitalize() == "Pounds":
  pounds = float(input("Please enter the amount of pounds: "))
  euros = pounds * 1.14
  print("The amount of euro is: ", euros)
if currency.capitalize() == "Euro":
  euros = float(input("Please enter the amount of euros: "))
  pounds = euros * 0.87
  print("The amount of pounds is: ", pounds)