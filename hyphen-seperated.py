import re
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow
strArray=input("enter hyphen seperated strings")
listStr=strArray.split("-")
listStr.sort()
strSort=""

for i in listStr:
    if strSort=="":
        strSort=i
    else:
        strSort=strSort+"-"+i

print(strSort)