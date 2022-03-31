seconds = int(input("Enter number of seconds: "))
minutes = int(input("Enter number of minutes: "))
hours = int(input("Enter number of hours: "))

totalSeconds = seconds + 60*minutes + 3600*hours
print (f"The total number of seconds is {totalSeconds}")
