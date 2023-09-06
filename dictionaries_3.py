#Given this dictionary:

ski_runs = {"easy": "green", "intermediate": "blue", "advanced": "black"}
#What does the following expression evaluate to?

ski_runs["expert"]
# KeyError: 'expert' Correct! There is no "expert" key in the dictionary, so Python raises a KeyError

#Given this dictionary:

ski_runs = {"easy": "green", "intermediate": "blue", "advanced": "black"}
#What does the following expression evaluate to?

"blue" in ski_runs
# False : Correct! "blue" is a value in the ski_runs dictionary, but the in operator only looks at the keys!

#Given this dictionary:

ski_runs = {"easy": "green", "intermediate": "blue", "advanced": "black"}
#What does the following expression return?

ski_runs.get("expert")
# None : Correct! The get() method returns None when a key is not found in the dictionary.