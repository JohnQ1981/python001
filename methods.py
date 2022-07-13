print("*** Welcome to Methods in Python ***")
f_name=input("Enter Your First Name and we will capitalize \n")
print("Your First name is "+ str(f_name.capitalize()))
l_name=input("Enter Your Last name and we will capitalize \n")
print("Your First name is "+ str(l_name.capitalize()))
print("Your full name is in Upper Cases "+ str(f_name.upper()+ " "+ l_name.upper()))
print("Your full name is in Lower Cases "+ str(f_name.lower()+ " "+ l_name.lower()))
country ="Algeria"
print(country.upper())
# strip() removes space by default.
textwithspace="   Hello World     "
print(textwithspace.strip())
hello="-----hello --------"
print(hello.strip("-"))
h2=",.,.,.,.,.,.hello,.,.,.,.,.,.a,a,b,b,b"
print(h2.strip(",. ab"))
print(h2.rstrip(",."))