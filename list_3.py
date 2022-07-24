wait_list = ['tom','ali','veli']
print(wait_list)
nums = [1,2,3,4,5,6,7]
print(nums)
nums.clear()  #clear() does clear the list. 
print(nums)
nums = [1,2,3,4,5,6,7]
wait_list.remove('ali') # remove()  removes the provided and matched element from the list
print(wait_list)
print(nums)
langs = ['Python','C', 'JavaScript','c']
langs.pop() # pop() removes and returns the last element from the list
print(langs)
langs.extend('JAVA')
langs.insert(-1,'JAVA')
langs.append('Ruby')
print(langs)
# the del Statement (it is not a method) can be used to delete an item from a specific index  in  a list
del langs[3]
print(langs)
del langs[3:5]
print(langs)
del langs[4]
print(langs)
langs.pop(4)
print(langs)