def is_harshad_num(num):
    num2=num
    add=0
    while 0<num:
        a=num%10
        add+=a
        num=num//10
    if num2%add==0:
        return "true"
    else:
        return "False"
num=int(input("enter the num"))        
print(is_harshad_num(num))           

