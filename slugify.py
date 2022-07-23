def slugify(n):
    return n.lower().strip().replace(" ", "-")

print(slugify("    Hello World   I love you"))