import art
from translate import Translator
print(art.art('woman'))
print(art.art('butterfly'))
print(art.art('bat'))
print(art.art('lion'))
print(art.art('tiger'))

print(art.text2art("HelloWorld"))

print(art.text2art("Hello", font='block'))

translator = Translator(to_lang="tr")
translator1 = translator.translate("This is a pencil")
print(translator1)