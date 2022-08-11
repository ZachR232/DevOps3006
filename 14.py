import ast

b = haim
my_file = open("config.json")
c = dict(ast.literal_eval(my_file.read()))

with open("names.txt") as my_file:
    for name in my_file.readlines():
        print(name.strip())

# with is creating a temporary scope after that the file is closed

