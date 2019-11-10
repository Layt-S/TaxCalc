import sys


startV = 1
res = str(input("Do you agree to the terms in README.dm, y/n: "))
res.lower()
while (startV == 1):
  if (res.lower() == "y"):
    startV = 2
    continue
  else: 
    str(input("Then press anything to exit the program: "))
    sys.exit()
  
#initialization the value
sumOfBrutto = 0
brutto = 0

#get user tax percentage input
taxPercentage=int(input("Entry your current tax percentage: "))
  
#handling exception
if (taxPercentage <= 0):
  print("The city wont grow it all by itself")
  sys.exit()


print("Entry all you brutto bills or invoices into the program, input a negative value to calculate")

repp= 0
var = 1
while var == 1:         #creating infinitive loop

  brutto = int(input()) #get user brutto input
  if (brutto<0):        #breaking loop
    break
  #handling exceptions
  if (brutto==0):
    print("In this world nothing is for free")
 
  
  sumOfBrutto += brutto #summing up the brutto sum
  
  repp+=1
  if (repp == 5):
    repp = 0
    print("Entry another bills or entry a negative value to calculate")
  
#calculations
taxPercentage = taxPercentage / 100 + 1
nettoValue = sumOfBrutto/taxPercentage
taxValue = sumOfBrutto-nettoValue
#printing calculations
print("Brutto value: ", round(sumOfBrutto, 2),"€")
print("Netto value: ", round(nettoValue, 2), "€")
print("Tax value: ", round(taxValue, 2), "€")

#exiting command (for sure)
var=int(input("Press anything to exit program: "))