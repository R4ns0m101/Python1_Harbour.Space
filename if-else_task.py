x = int(float(input()))

if x % 2 == 0:
    if x % 3 != 0:
        print("B")
    else:
        print("C")
else:
    print("D")