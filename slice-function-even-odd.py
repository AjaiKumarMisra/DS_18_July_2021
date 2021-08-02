import math

listN=[]
posList=[]
counter=50
x=0
for x in range(0,50):
    listN.append(x)
print(listN)
# mid_pos=int(50/2)
# 
# countmid=int(input("please enter middle numbers count"))
# 
# 
# 
# countS=mid_pos-math.floor(countmid/2)
# countE=mid_pos+math.ceil(countmid/2)


x=slice(2,counter,+2)
#for i in range(countS,countE):
print("Even number")
print(listN[x])

print("Odd Number")
x=slice(1,counter,+2)
print(listN[x])

