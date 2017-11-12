rows = int(input("introduce the number of rows: "))
col = int(input("introduce the number of columns: "))
s_row = int(input("introduce the starting row: "))
s_col = int(input("introduce the starting coumn: "))

"""
case 1: from upper right corner:
"""

if s_row == 1 and s_col == 1:
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


"""
case 2: from upper left corner:
"""

if s_row == 1 and s_col == col:
    i = 1
    x = col
    while i <= rows:
        if i % 2 == 1:
            j = 1
            while j <= col:
                print(x)
                x -= 1
                j += 1
            i += 1
        else:
            j = 1
            while j <= col:
                print(x)
                x += 1
                j += 1
            x -= 2
            i += 1
        x += col+1

"""
case 3: from lower left
"""

if s_row == rows and s_col == 1:
    i = 1
    x = rows * col
    x -= col
    x += 1
    while i <= rows:
        if i % 2 == 1:
            j = 1
            while j <= col:
                print(x)
                x += 1
                j += 1
        else:
            j = 1
            while j <= col:

                x -= 1
                print(x)
                j += 1

        i += 1
        x -= col

"""
case 4: from lower right
"""

if s_row == rows and s_col == col:
    i = 1
    x = rows * col
    while i <= rows:
        if i % 2 == 1:
            j = 1
            while j <= col:
                print(x)
                x -= 1
                j += 1
        else:
            j = 1
            while j <= col:

                x += 1
                print(x)
                j += 1

        i += 1
        x -= col
