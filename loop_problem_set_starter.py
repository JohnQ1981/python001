
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable
for c in word :
    print(c)

print("*"*50)

# Write a while loop that does the same thing!
count = 0
while count < len(word):
     print(word[count])
     count +=1

#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)

count =100
while count <= 140 :
        print(count)
        count +=2


print("*"*50)
# Write a for loop that does the same thing (with range())
for c in range(100,141,2):
    print(c)
#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:
phrase = input("Enter :'sillygoose' ")
while phrase !="sillygoose":
    phrase = input("Enter :'sillygoose' ")

print("You did it")
