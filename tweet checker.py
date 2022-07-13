print('*'*40)
print('*** WELCOME TO TWEET CHECKER APP ***')
max_char=140
tweet= input('Enter Your tweet:\n')
char_count=len(tweet)
if char_count <max_char :
    print(f'That {char_count} char tweet will work')
elif char_count >max_char :
    print(f"I'm sick and tired of people littering and leaving their garbage all over beautiful places!\n Why are so many people such unbelievable morons ???? ")
    print(f'Your {char_count} char tweet is {char_count-max_char} chars too long')
else :
    print('You have exactly 140 chars')
