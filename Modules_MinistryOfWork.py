from textblob import TextBlob
import pyttsx3
engine = pyttsx3.init()
import art
#print(art.text2art("welcome to ministry of work"))
print(art.text2art("Hello", font='block'))
engine.say("Hello John, Employee number 256. we hope you had a great day of work. It's time to submit your employee wellness statement")
engine.runAndWait()
blob = TextBlob("I really hate you ugly guy!")
print(blob.sentiment)
print(blob.sentiment.polarity)
print(blob.sentiment.subjectivity)

blob2 = TextBlob("Weather is Hot in Summer")
print(blob2.sentiment)
print(blob2.sentiment.polarity)
print(blob2.sentiment.subjectivity)

print("Enter Your employee wellness statement :")
phrase = input(">")
user = TextBlob(phrase)
print(user.sentiment)
print(user.sentiment_assessments)
while user.sentiment.polarity < 0.5:
    #print("Try to be more positive please :")
    engine.say("""Hey John, Employee number 256, that was not a very positive employee wellness statement. Please 
    Try to be more positive. we know how much you love working here. :""")
    engine.runAndWait()
    phrase = input(">")
    user = TextBlob(phrase)

engine.say("""Hey John, Employee number 256, Awesome, we do appreciate you as well! You can leave now, 
have a great rest of the day. Thank you for a such a kind and positive statement. we here are the ministry of work appreciate you too! """)
engine.runAndWait()
print("Awesome, we do appreciate you as well!")


#engine.say("I will speak this text")
#engine.runAndWait()
