ski_runs = {"easy": "green", "intermediate": "blue", "advanced": "black"}
pop_val = ski_runs.pop('easy') #pop() method deletes key provided
#print(ski_runs)

#ski_runs.pop() # needs argument: Key
print(ski_runs) #{'intermediate': 'blue', 'advanced': 'black'}
print(pop_val) #green
 # popitem() method deletes the most recently added key-value pair. it returns the item as a tuple.

pop_item = ski_runs.popitem()
print(ski_runs) #{'intermediate': 'blue'}
print(pop_item) # as Tuple : ('advanced', 'black')

ski_runs['hard'] = 'blue'
print(ski_runs)

#clear() method deletes all items for a dictionary. It Returns None.

ski_runs['hard'] = 'blue'
print(ski_runs)
del ski_runs['hard']
print(ski_runs)
ski_runs.clear()
print(ski_runs)