import requests
print("moshe")
try:
    r = 5 / 9
except ZeroDivisionError:
    print("could not divide by zero")
except ValueError:
    print("enter a legal number")
except BaseException as e:
    print("something went wrong, here is more")
    print(e.args)
print("haim")
