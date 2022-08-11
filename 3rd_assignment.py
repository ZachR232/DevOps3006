# 1 + 2

try:
        a = 1 / 0
except:
    print("Division by zero")
# 3 yes - finally can come after any kind of "try"
try:
    x = 1
finally:
    print("Finally!")

# 4 - Except handles all types of exceptions

# 5 - this exception is broad, and does not specify to a specific scenario

# 6
# except IOError - occurs when a file, file path, or OS operation we're referencing does not exist.
# except ZeroDivisionError - when a number is divided by a zero.

# 7
my_file = open("text.txt", 'w')
my_file.close()

# 8
my_file = open("text.txt", 'a')
my_file.write("Zach")
my_file.close()

# 9
my_file = open("text.txt", 'a', encoding='utf-8')
my_file.write(" עברית שפה יפה ")
my_file.close()







