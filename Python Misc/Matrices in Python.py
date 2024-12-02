def matrix_takein(name):
    print()
    row = int(input(f"Enter the no. of rows in Matrix {name}: "))
    column = int(input(f"Enter the no. of columns in Matrix {name}: "))
    print()
    return matrix_create(row, column, name)


def matrix_create(row, column, name):
    matrix = []
    for i in range(row):
        row = []
        for j in range(column):
            element = int(input(f"Enter the element on Matrix {name} [{i}][{j}]: "))
            row.append(element)
        matrix.append(row)
    matrix_print(matrix, name)
    return matrix


def matrix_print(mx, name):
    print(f"\n{name} = ")
    for i in mx:
        print(i)


def matrix_combo(mx, my, sign):
    if len(mx) == len(my) and len(mx[0]) == len(my[0]):
        result_mx = []
        for i in range(len(mx)):
            result_row = []
            for j in range(len(mx[0])):
                element = eval(f"{mx[i][j]} {sign} {my[i][j]}")
                result_row.append(element)
            result_mx.append(result_row)
        return matrix_print(result_mx, "Result")
    else:
        print("\nProvided matrices are of unequal sizes!")


def matrix_mul(mx, my):
    if len(mx[0]) == len(my):
        result_mx = []
        for i in range(len(mx)):
            result_row = []
            for j in range(len(my[0])):
                element = 0
                for k in range(len(my)):  # or len(mx[0])
                    element += mx[i][k] * my[k][j]
                result_row.append(element)
            result_mx.append(result_row)
        return matrix_print(result_mx, "Result")
    else:
        print("\nProvided matrices are invalid for multiplication!")


print(
    """\nWhat operation you want to conduct ?
    1. Addition
    2. Subtraction
    3. Multiplication\n"""
)
choice = int(input("Choose number from above: "))
ma = matrix_takein("A")
mb = matrix_takein("B")

operations = ["0", "+", "-", "*"]

if choice == 1:
    pass
else:
    print(
        f"""\nYou want to operate like?
        1. A {operations[choice]} B
        2. B {operations[choice]} A\n"""
    )
    orientation = int(input("Choose number from above: "))

if orientation == 2:
    prop_1 = ma
    prop_2 = mb
    ma = prop_2
    mb = prop_1

if choice == 3:
    matrix_mul(ma, mb)
else:
    matrix_combo(ma, mb, operations[choice])
