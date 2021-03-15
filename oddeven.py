def add(list):
    i=0
    even=[]
    odd=[]
    while i<len(list):
        if list[i]%2==0:
            even.append(list[i])
        else:
            odd.append(list[i])
        i+=1
    print(even) 
    print(odd)
list=[12,45,56,99,89]
add(list)

            





