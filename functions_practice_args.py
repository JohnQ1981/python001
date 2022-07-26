def contains_pickle(*args):
    lst=[]
    lst.append(args)
    for c in lst:
        print(c)
        if c == "pickle":
            return True
        else:
            return False

test = contains_pickle('pickle',2,'joke','hello','pickle')
print(test)
def count_fails(*args):
    if int(args).isnumeric():
        lst=list(args)