i = 0 # Loop the script
while i != 1:
    menu = int(input("Type 1 for Fahrenheit to Celsius, Type 2 for AUD to USD, Type 3 for kilometres to miles: ")) # Reads input as an integer and redirects to the appropriate conversion formula
    if menu == 1: #Saying that if the input value entered at the menu is 1, that the program will run for the fahrenheit. The same applies for the other two conversion forumlas
        fahrenheit = float(input("Enter Fahrenheit temperature: ")) 
        celsius = 5*(fahrenheit - 32)//9 # conversion formula for degrees celsius to degrees fahrenheit

        print (f"The temperature in Celsius is {celsius}")

     # elif is used instead of else due to there being multiple options
    elif menu == 2:

        aud = float(input("Enter Amount of AUD: "))
        usd = 1.35*(aud)
    
        print (f"The converted amount to USD is ${usd} ")

    elif menu == 3:
        km = float(input("Enter length in kilometres: "))
        mi = 1.6*(km)

        print (f"The length of Kilometres in miles is {mi} ")


    restart = input("Would you like to continue? Yes(y) or No(n) ")
    if restart == "Yes" or restart == "Y" or restart == "yes" or restart == "y":
        print("Ok")
    elif restart == "No" or restart == "N" or restart == "no" or restart == "n" :
        print("Ending Program")
        break
#Script will keep running until the user inputs "No", at which point the module will stop running
