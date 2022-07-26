# Intersection returns new set with members common to left and right 
set1 = {1,2,'g',3,4,5,6,'rr'}
set2 = {1,2,3,4,5,6,7,8,9,'rr'}
intersection_set = set1 & set2
print(intersection_set)
#Union returns new set with members from left and right with no duplicates

union_set = set1 | set2
print(union_set)
# Difference returns new set with members from left not in right, so order does matter

difference_set = set1 - set2
print(difference_set)

difference_set2 = set2 - set1
print(difference_set2)