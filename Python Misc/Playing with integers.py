num = int(input("Enter the no: "))
num_ = num
count = 0
rev = 0
while num_ >= 1:
    num_ /= 10
    count += 1

print(f"Number of digits in the integer: {count}")

num_ = num
for i in range(0, count):
    remainder = num_ % 10
    quotient = num_ // 10
    count -= 1
    rev += remainder * (10 ** (count))
    num_ = quotient

print(f"The integer {num} but reversed: {rev}")
