#Using iter function print only even and odd numbers of a list between 1 to 100
listN=range(1,101)


listN1=iter(listN)
print("Event Number")
for i in listN:
    if i%2==0:
        print(next(listN1))
    else:
        next(listN1)
        
print("Odd Number")
listN2=iter(listN)
for i in listN:
    if i%2!=0:
        print(next(listN2))
    else:
        next(listN2)