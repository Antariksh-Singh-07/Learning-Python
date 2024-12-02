def volume(l=1, w=1, h=1):
    return l * w * h

Length = float(input("Enter Length: "))
Width = float(input("Enter Width: "))
Height = float(input("Enter Height: "))

print(f"The Volume of the given Dimensions will be {volume(Length, Width, Height)}")