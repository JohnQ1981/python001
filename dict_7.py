test_scores = {
    'Ali': 98,
    'veli': 85,
    'Celi': 75,
    'Deli': 79,
    "kali": 88,
    'Hali':97
}
#find max
max_val = 0
min_val = 0
student_max =""
student_min = ""
for key, values in test_scores.items():
    print(f"Key is {key}, Value is : {values}")
    if values > max_val:
        max_val = values
        min_val = max_val
        student_max = key
    if values < min_val:
        min_val = values
        student_min =key
    
print(f"The max is {max_val} and Student is {student_max}, and Min is {min_val} and Student is {student_min} ")
