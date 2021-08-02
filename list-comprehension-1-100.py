#Using list comprehension, create a list of even and odd numbers between 1 to 100


listEven=[]
listOdd=[]

listEven=[x for x in range(1,100) if x%2==0]

listOdd=[x for x in range(1,100) if x%2!=0]
print("Even List")
print(listEven)
print("Odd List")
print(listOdd)

