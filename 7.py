x_boom = 7
for i in range(1, 101):
    if i % x_boom != 0 and str(x_boom) not in str(i):
        print(i)
else:
    print("loop finished successfully")


