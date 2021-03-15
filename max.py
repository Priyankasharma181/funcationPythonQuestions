# numbers = [3, 5, 7, 34, 2, 89, 2, 5] 
# c=max(numbers)
# print(c)

# max number
def max(list1):
    index=0
    max=list1[1]
    while index<len(list1):
        m=list1[index]
        if m>max:
            max=m
        index+=1
    return max    

i = 0
list1 = []
user = int(input("how many element you want in list"))
while i <user:
    user1 = int(input("enter your list element which you want to include in your list"))
    list1.append(user1)
    i = i + 1
print(list1)
print(max(list1))

    