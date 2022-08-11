is_true = False
a = 2
b = 2.5
strOne = "One"
strThree = "Three"
names = ["Chanan", "Tome", "Zack", "Aharon"]
print(type(a == b))
if a < b and strOne == "moshe" or strThree == "Three":
    print("a is smaller then b")
elif a == b:
    print("a equals b")
elif b > 1:
    print("blabla")
else:
    print("something")

other_list = []
name_to_find = "Ariel"
if name_to_find in names:
    print(f"{name_to_find} is on the list")
else:
    print(f"{name_to_find} is not on the list")

if len(other_list) > 0:
    print("other list has values")

k = 5
f = 5
t = [1, 2, 3]
e = [1, 2, 3]
if type(k) is int:
    print("I like boys")
elif type(k) is str:
    print("I like strings!")
print(k is f)
print(t == e)
print(t is e)




