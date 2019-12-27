#This program will convert Fahrenheit to Celsius and vis versa.
#Made by Cody Grande.
#This program was made for practice purposes and exists without any license, do what you will with it.
#This was uploaded to github / Gitlab to help the Author figure out how to use Github / Gitlab.


tempChoice = input("Please type c to convert from Celsius or f to convert from Fahrenheit.\n")
endTemp = 0 #so program knows endTemp is an int.
testTemp = 0 #I needed a int for a workarround sooooo...

while tempChoice not in 'cCfF': # Simple user input sanitation
    print("wrong input detected") # If user hits enter without any input the program crashes. Need to fix.
    tempChoice = input("Please type c to convert from Celsius or f to convert from Fahrenheit.\n")

#This will let us repeat there start temperature type (F or C)  when getting user input for startTemp
if (tempChoice =='c') or (tempChoice == 'C'):
    tempType = 'Celsius'
else: # Gotta love else, it lets us be a bit lazy.
    tempType = 'Fahrenheit'

#Decided to place after user sanitation, just to get the temp to convert from.
startTemp = input("Please enter the temperature in {}.\n".format(tempType))

#note to self, create user input sanitation here.

# C = (F - 32) / 1.8
# F = C * 1.8 + 32

if tempType == 'Celsius': # keeping it simpel and avoiding the or as seen above.
  endTemp = (int(startTemp) * 1.8) + 32
  print("The temperature in Fahrenheit is {} °F.".format(endTemp))
else:
    endTemp = (int(startTemp) -32) / 1.8
    print("The temperature in Celsius is {} °C.".format(endTemp))
