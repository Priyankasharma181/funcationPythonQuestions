# print("*****swagat hai aap ka kon banega karorpati*****")
# print("                     ")
# print(".......yeh rha question aapki screen par.........")
def kbc(question,option,i ,t1,lol,count,solution):
    i = 0
    while i<len(question):
        print(question[i])
        j=0
        k=1
        while j<len(option):
            print(k,".",option[i][j])
            j+=1
            k+=1
        z=["3.wikipedia","4.google","2.bhopal","1.four","2.two","1.narendra modi","2.amitshah"]
        use=input("do you want life line yes/no ")
        if use=="yes":
            print("50-50")
            if count==0:
                print(z[i+t])
                print(z[i+t])
                ans=int(input("enter the num"))
                if ans==solution[i]:
                    print("shi jwab")
                    print("bhadai ho aapne jite hai ",lol)
                    count+=1
                else:
                    print("galt jawab, game over")
                    break
            else:
                print("aapne life line use kar liya")
                ans=int(input("enter the num"))
                if ans==solution[i]:
                    print("she javab")
                    print("bdhai ho aap ne jite hai",lol)
                else:
                    print("game over")
                    break
        elif use=="no":
            user=int(input("enter the answer"))
            if solution[i]==user:
                print("shi  jawab")
                print("bhdai ho aapne jite")
            else:
                print("game over",)
                break
        else:
            print("glat jawab")
        lol+=10000

        t+=1
        t1+=1
        i+=1
kbc([
    "which of the follwing is not socal networking site?",
    "what is the capital of india?",
    "in the game of ludo the discs or token are of how many clours?",
    "who is the prime ministar of india from 2014 to 2019",

],["twitter","facebook","wikipidia","google+"],
["chndigarh","bhopal","chennai","dehli"],
["four","two","three","one"],
["amit shah","narendra modi","udhhav tahkre","shivrajsingh chouan"],[0,0,1,10000,0],[3,4,1,2])                


                





