import email


emails = ['a@gmail.com', 'ab@gmail.com','abc@gmail.com','abcd@gmail.com','abcde@gmail.com','abcdef@gmail.com','abcdefg@gmail.com',]
print(emails)
for c in emails :
    print(f'*** SENDING EMAIL TO: {c}')
    #print(c)
idx = 0

while idx < len(emails):
    print(f'{emails[idx]} is email that is being printed')
    idx +=1

print('done')

count = len(emails)-1
c = 0
while count >=0:
    c += 1
    print(f'the {c}" : {emails[count]} is email that is being printed')
    count -=1
    
print("Done second time")