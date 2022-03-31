m = 10
n = 3
print (m < n)
print (m == n)
print (0 < n <= 5)


print(m < 0 or 5 < m)
print (not m == n)
print (not m >= n)
print (0 < n and n <= 5)


n = int(input("Enter an integer:"))
if n % 2 == 0:
        print (f"{n} is even")
else:
    print (f"{n} is odd")



text = str(input("Enter a string"))
n = int(input("Enter an integer"))

if 0 < n < 10:
    # print string n times
    print (text * n)
