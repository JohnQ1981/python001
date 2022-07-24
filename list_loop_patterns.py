lando_2021_results = [4,3,5,8,3,5,5,5,3,4,14,10,2,7,7,8,10,10,9,10,7]
count = 0
idx =len(lando_2021_results)
for c in lando_2021_results:
    count = count + c
    

print(count)
print(f"The average is {int(count/idx)}, and total is : {count}")

def average (nums):
    total = 0
    for num in nums:
        total += num
    return total/len(nums)

print(average(lando_2021_results))

#find min 
min = lando_2021_results[0]
for c in lando_2021_results:
    if c < min:
        min = c
print(F"the minimum is {min}")

#find max
max = lando_2021_results[0]
for j in lando_2021_results:
    if j > max:
        max = j

print(f"The maximum is {max}")