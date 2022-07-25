from tkinter.filedialog import test


test_scores = {
    'Ali': 98,
    'veli': 85,
    'Celi': 75,
    'Deli': 79,
    "kali": 88,
    'Hali':97
}
for c in test_scores.keys():
    print(c)

for j in test_scores.values():
    print(j)

total = 0
for scores in test_scores.values():
    total = total + scores
print(f"Average of the scores is {total/len(test_scores)}")
print(f"Average of the scores is {total/len(test_scores.keys())}")
print(len(test_scores.values()))

for item in test_scores.items():
    print(item)
print("Above are items ", '*'*40)

for key, value in test_scores.items():
    print(key, value)
print("Above are Unpacked ", '*'*40)