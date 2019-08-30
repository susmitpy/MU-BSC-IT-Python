try:
    a = 5/0
except ZeroDivisionError as e:
    print(e)
finally:
    b = 4/2
    print(b)