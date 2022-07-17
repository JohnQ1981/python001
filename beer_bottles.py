for c in range(100,0,-1):
    print(f"{c} bottles of beer on the wall")
    print(f"{c} bottles of beer")
    if c ==1:
        print(f"Take one down, pass it around, no bottles of beer on the wall")
    else:
        print(f"Take one down, pass it around, {c-1} bottles of beer on the wall")
        print("*"*40)

count = 100
while count > 0 :
    if count == 1:
        print(f"{count} bottle of beer on the wall")
        print(f"{count} bottle of beer")
        #print(f"Take one down, pass it around, {count-1} bottles of beer on the wall")
        print(f"Take one down, pass it around, no bottle of beer on the wall")
    elif count == 2:
        print(f"{count} bottles of beer on the wall")
        print(f"{count} bottles of beer")
        print(f"Take one down, pass it around, {count-1} bottle of beer on the wall")
    else:
        print(f"{count} bottles of beer on the wall")
        print(f"{count} bottles of beer")
        print(f"Take one down, pass it around, {count-1} bottles of beer on the wall")
        print("*"*40)
        print("-"*40)
    count -= 1