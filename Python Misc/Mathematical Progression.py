# 1. x¹/1! + x²/2! + x³/3! + x⁴/4! +... xⁿ/n!
# 2. x¹/1! - x²/2! + x³/3! - x⁴/4! +... xⁿ/n!
# 3. 1¹/1! + 2²/2! + 3³/3! + 4⁴/4! +... nⁿ/n!
# 4. sinx = x - x³/3! + x⁵/5! - x⁷/7! +...
# 5. cosx = 1 - x²/2! + x⁴/4! - x⁶/6! +...


def fact(n):
    if n in (0, 1):
        return 1
    else:
        return n * fact(n - 1)


x = int(input("Input x: "))
n = int(input("Input n: "))

series_1 = series_2 = series_3 = series_4 = series_5 = 0

# Series I
for i in range(1, n + 1):
    series_1 += x**i / fact(i)

# Series II
for i in range(1, n + 1):
    series_2 += (-1)**(i-1)*(x**i / fact(i))

# Series III
for i in range(1, n + 1):
    series_3 += i**i / fact(i)

#Series IV
for i in range(n):
    series_4 += (-1)**(i)*(x**(2*i+1) / fact(2*i+1))

#Series V
for i in range(n):
    series_5 += (-1)**(i)*(x**(2*i) / fact(2*i))

print(f"Series 1 = {series_1} \nSeries 2 = {series_2} \nSeries 3 = {series_3} \nSeries 4 = {series_4} \nSeries 5 = {series_5}")
