def display_info(person,*args, status="single"):
    print(f"person is:{person}")
    print(f"status is:{status}")
    print(f"person is:{args}")

print(display_info('John',25,2,3,66,55,66))

def display_info(person,*args, status="single",**kwargs):
    print(f"person is:{person}")
    print(f"status is:{status}")
    print(f"person is:{args}")
    print(f"person is:{kwargs}")
    print(f"status is:{status}")

print(display_info('John',25,2,3,66,55,66, mood='happy', status='married'))