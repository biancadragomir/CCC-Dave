rows = int(input("introduce the number of rows: "))
col = int(input("introduce the number of columns: "))

i = 1
x = 1
while i <= rows:
    if i % 2 == 1:
        j = 1
        while j <= col:
            j += 1
            print(x)
            x += 1
        i += 1
    else:
        j = 1
        while j <= col:
            x += 1
            j += 1
        j = 1
        while j <= col:
            j += 1
            x -= 1
            print(x)
        j = 1
        while j <= col:
            x += 1
            j += 1
        i += 1
