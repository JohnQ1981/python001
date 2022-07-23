def laugh(str=2):
    print("HA!"*str)

laugh(5)
laugh()
def slugify(n, sep="-"):
    return n.lower().strip().replace(" ", sep)
print(slugify("    hello world chicken   ola    ","_"))