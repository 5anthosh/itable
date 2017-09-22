def maxium(row):  # find greatest in giver row
    max1 = 0
    for j in row:
        if max1 < len(str(j)):
            max1 = len(str(j))
    return max1


def maxi(table1):  # for given box find greatest value in every row
    max1 = []
    for j in table1:
        max1.append(maxium(j))
    return max1


def greatest(table1):
    max1 = 0
    for i in table1:
        if max1 < len(i):
            max1 = len(i)
    return max1


def line(table, k='-', c='+'):
    m = maxi(table)
    for i, j in enumerate(m):
        print(c, k * (int(j)) + k + k, sep='', end='')
        if i == len(m) - 1:
            print(c)


def cTable(table, header=False):
    """/
    print by columns

    """
    m = maxi(table)
    column = 0  # for column
    row = 0  # for row
    g = greatest(table)
    while row < g:
        if row == 0 or row == 1:
            if header:
                line(table, '=')
            else:
                line(table)
        else:
            line(table)
        for j in table:
            if row <= len(j) - 1:
                print('| ', str(j[row]), ' ' * (m[column] - len(str(j[row])) + 1), sep='', end='')
                column = column + 1
            else:
                print('|  ', ' ' * (m[column]), sep='', end='')
                column = column + 1
            if column == len(table):
                print('|')
                row = row + 1
                column = 0
            if row == g:
                line(table)


def rTable(table,header=False):
    """
    print by column
    """
    cTable(list(zip(*table)), header=header)