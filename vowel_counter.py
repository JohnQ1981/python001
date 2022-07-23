def vw(n):
    count = 0
    for c in n:
        if c in "aeiou":
            count +=1
    return count
while True:
    vv=input("enter string ")
    print(vw(vv))
    again=input("do you want to continue")
    if again == "y" or again =="Y":
        continue
    elif again =="n" or again == "N":
        break
    else:
        print("Enter ony y or n")
    
        

