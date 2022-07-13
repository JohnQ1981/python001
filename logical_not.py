print("*"*30)
print("Welcome to not logical expression")
year= input("What year were you born in? ")
if not year.isnumeric():
    print("looks like you entered not correct year try again")
    year= input("What year were you born in? ")



year=int(year)
print(f" You were born {2022-year} years ago")


