from random import randint
num = int(input("Enter Number that should match random \n"))
randy = randint(0,10)
while num != randy:
    num = int(input("Try Again \n"))
    if num == randy:
        break
    
    
print(randy)

word = "Hello World"
for c in word:
    if c == "W":
        break
    print(c)

for c in word:
    if c in "aeiou":
        continue
    print(c)