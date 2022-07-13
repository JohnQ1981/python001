# strip() removes space by default.
textwithspace="   Hello World     "
print(textwithspace.strip())
hello="-----hello --------"
print(hello.strip("-"))
h2=",.,.,.,.,.,.hello,.,.,.,.,.,.a,a,b,b,b"
print(h2.strip(",. ab"))
print(h2.rstrip("a,."))
print(h2.rstrip("a,.b"))
print(h2.lstrip("a,.b"))
# str.replace()  Replace method ,
r="Hello World"
print(r.replace("Hello","World"))
races="3km 6km 10km"
print(races.replace('km','kilometers'))
prices="$1.99, $2.99, $3.99"
print(prices.replace('$',''))
#find method
cat="Cat in a Hat"
print(cat.find('a'))
print(cat.find('a', 5))
#count method
print(cat.count("a"))
