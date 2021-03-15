def duplicat(list):
    i=0
    j=1
    a=[]
    b=[]
    while i<len(list):
        if list[i]==list[j]:
            a.append(list)
            print(a)
        else:
            b.append(list)  
    
    print(b)
list=[7,9,5,4,7,5,7,7]    
duplicat(list)              

