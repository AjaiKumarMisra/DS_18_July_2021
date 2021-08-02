# Write a Python program to add new Key,Value pair in {"A":2,"B":3} dictionary. Get the input "KEY" and "VALUE" from user and add to the dictionary.
# If entered KEY is existing then dont overwrite existing KEY:VALUE but print some warning message else add as new KEY/VALUE pair

dictN={"A":2,"B":3}
kName=input("Enter KEY name")
vName=input("Enter Value")

for i in dictN.keys():
    if kName==i:
        print("Provided Key Name is already exists")
        status="found"
    else:
        status="Not"
        
if status=="Not":
    dictN.update({""+kName+"":vName})

print(dictN)