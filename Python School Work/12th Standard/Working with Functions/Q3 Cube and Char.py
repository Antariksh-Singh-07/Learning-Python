def cube(x=2):
    print(f"{x}³ = {x**3}")
def char(x, y):
    if x == y:
        return True
    else:
        return False
choice = input("You want to access cube or char program [1/2]: ").lower()
if choice == ("1" or "cube"):
    input_cube = input("Enter a number: ")
    if input_cube == "":
        cube()
    else:
        cube(float(input_cube))
elif choice == ("2" or "char"):
    char_1 = input("Input 1st Character: ")
    char_2 = input("Input 2nd Character: ")
    print(char(char_1, char_2))
else:
    print("Small Chin Chin! (this translates to small penis, don't write this, write a error message instead)")
