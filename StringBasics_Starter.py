# create two variables
first_name="John"
print(first_name)
last="Quchkarov"
print(last)
full_name= first_name + " " + last
print(full_name) 
initials= full_name[0] + last[0]
print(initials)
initials_2 =full_name[0] +","+ last[0]
print(initials_2)

nickname= first_name[0:5]
nickname_2= last[:5]

print(nickname)
print(nickname_2)
type(nickname)
print(len(nickname))
print(len(full_name))