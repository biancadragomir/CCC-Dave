rows = int(input("introduce the number of rows: "))
col = int(input("introduce the number of columns: "))
s_row = int(input("introduce the starting row: "))
s_col = int(input("introduce the starting coumn: "))
d = input("direction: ")

"""
case 1: from upper left corner, direction EAST
"""

if s_row == 1 and s_col == 1 and d == 'e':
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
case 2: from upper right corner, direction WEST:
"""

if s_row == 1 and s_col == col and d == 'w':
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
case 3: from lower left, direction EAST
"""

if s_row == rows and s_col == 1 and d == 'e':
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
case 4: from lower right, direction WEST
"""

if s_row == rows and s_col == col and d == 'w':
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

"""
case 5: upper left, direction SOUTH
"""

if s_row == 1 and s_col == 1 and d == 's':
    i = 1
    x = 1
    while i <= col:
        if i % 2 == 1:
            j = 1
            while j <= rows:
                print(x)
                j += 1
                x += col

        else:
            j = 1
            x -= col
            while j <= rows:
                print(x)
                x -= col
                j += 1
            x += col

        x += 1
        i += 1

"""
case 6: upper right, direction SOUTH
"""

if s_row == 1 and s_col == col and d == 's':
    i = 1
    x = col
    while i <= col:
        if i % 2 == 1:
            j = 1
            while j <= rows:
                print(x)
                j += 1
                x += col

        else:
            j = 1
            x -= col
            while j <= rows:
                print(x)
                x -= col
                j += 1
            x += col

        x -= 1
        i += 1

"""
case 7: lower right, direction NORTH
"""

if s_row == rows and s_col == col and d == 'n':
    i = 1
    x = rows * col
    while i <= col:
        if i % 2 == 1:
            j = 1
            while j <= rows:
                print(x)
                x -= col
                j += 1
            x += col
        else:
            j = 1
            while j <= rows:
                print(x)
                x += col
                j += 1
            x -= col
        i += 1
        x -= 1

"""
case 8: lower left ,direction NORTH
"""

if s_row == rows and s_col == 1 and d == 'n':
    i = 1
    x = col * rows
    x -= col
    x += 1
    while i <= col:
        if i % 2 == 1:
            j = 1
            while j <= rows:
                print(x)
                j += 1
                x -= col
            x += col

        else:
            j = 1

            while j <= rows:
                print(x)
                x += col
                j += 1
            x -= col

        x += 1
        i += 1
