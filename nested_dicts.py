test_scores ={
    'semester1': {
    'Ali': 98,
    'veli': 85,
    'Celi': 75,
    'Deli': 79,
    "kali": 88,
    'Hali':97
},
'semester2': {
    'Ali': 88,
    'veli': 95,
    'Celi': 95,
    'Deli': 99,
    "kali": 98,
    'Hali':87
},
}
print(test_scores['semester1']['Ali'], test_scores['semester2']['Ali'])
print("*"*45)
print(test_scores['semester1'].items(), test_scores['semester2'].items())