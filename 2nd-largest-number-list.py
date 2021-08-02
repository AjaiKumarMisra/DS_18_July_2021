listN=[4,5,2,1,9,8,15,41,56,3]
largest=0
sec_lar=0
for i in listN:
    if largest<i:
        sec_lar=largest
        largest=i
    else:
        if sec_lar<i:
            sec_lar=i
            
print(sec_lar)         