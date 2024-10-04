#!/usr/bin/python3
"""Pascal triangle module"""


def pascal_triangle(n):
    """Pascal triangle of n"""
    triaangle = []                      # step 1
    for i in range(n):
        row = [0] * (i + 1)             # step 2
        triaangle.append(row)

        row[0] = row[-1] = 1            # step 3

        if i >= 2:                      # step 4
            for j in range(1, i):
                row[j] = triaangle[i - 1][j] + triaangle[i - 1][j - 1]

    return triaangle


"""
Example (n = 5)

**step 1: create empty triangle
triangle = []


**step 2: initialize the triangle's rows with 0
(columns number = row's index (i) + 1)
i = 0  => [0]
i = 1  => [0,0]
i = 2  => [0,0,0]
i = 3  => [0,0,0,0]
i = 4  => [0,0,0,0,0]   ([0] * 5 = [0,0,0,0,0])


step 3: update the first and the last number of each row with 1:
i = 0  => [1]
i = 1  => [1,1]
i = 2  => [1,0,1]
i = 3  => [1,0,0,1]
i = 4  => [1,0,0,0,1]


step 4: update middle numbers
(each digit must be the sum of the two upper digits from the previous row)
i = 0  => [1]
i = 1  => [1,1]
*** start from i = 2 ***
i = 2  => [1,2,1]
i = 3  => [1,3,3,1]

let's take i = 4 for instance:
i = 4  => row = [1,0,0,0,1] (initial value)

let's use j to iterate the row but remember!
* we don't have to change the first and the last numbers of the row
it means that j must start from 1 to 3 (the 3th index is 4 - 1 so i - 1)
* row[j] must be the sum of values at index j and j - 1 from previous row
previous row is triaangle[i - 1] (in our case it's triangle[3] = [1,3,3,1])


for j in range(1, i): (from 1 to i - 1)
row[j] = triaangle[i - 1][j] + triaangle[i - 1][j - 1]
j = 1 => row[1] = triangle[3][1] + triangle[3][0] = 3 + 1 = 4
row now is [1,4,0,0,1]

j = 2 => row now is [1,4,6,0,1]
j = 3 => row now is [1,4,6,4,1]

finally:
    i = 4  => row = [1,4,6,4,1] (final value)
"""


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
