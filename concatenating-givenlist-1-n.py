listN=["p","q"]
n=int(input("please provide end count to generate list with concatenation numbers with existing list"))

first=listN[0]
second=listN[1]


listN.clear()

for i in range(0,n):
    listN.append(first+str(i+1))
    listN.append(second+str(i+1))

print(listN)