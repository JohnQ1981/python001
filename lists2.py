waitlist = ['tom','ali','veli']
print(waitlist[1])
print(waitlist[2])
print(waitlist[0])
#waitlist += waitlist.sort()
print(waitlist)
waitlist.insert(0,'deli')
print(waitlist)
waitlist.append('celi')
print(waitlist)
waitlist.extend("abc")
print(waitlist)
people = ['juan','jorge',5,6,1.2,'helllo']
waitlist.extend(people)
print(waitlist)
waitlist.insert(2,'WORLD')
print(waitlist)
print(waitlist[2:4])
print(waitlist[2:])
print(waitlist[:4])
print(waitlist[::2])
# list[start:stop:step]