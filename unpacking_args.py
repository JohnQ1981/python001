def average(*args):
    total = 0
    for c in args:
        total += c
    return total/len(args)

print(average(2,5,6,4,5,6,5,6,66,695,85.5,95.36,952.365,55,66,55,852.325,74))

numbs = [7,5,6,3,2,1]
#print(average(numbs)) #Type Error
print(average(*numbs))