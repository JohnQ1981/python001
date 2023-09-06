nums = [1,2,3,4,5]
nums2 = nums.copy() # <---shallow copy-- nested objects are not copied
# it is called shallow copy
print(id(nums), "and", id(nums2))

# if you want to copy nested copy you need to use
# deep copy
import copy
list1 = [2,8,['a','b',2],7]
list2 = copy.deepcopy(list1)
print(list2)