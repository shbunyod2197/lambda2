# 1
f = lambda a, b: 0 if a == b else (1 if a > b else -1)
print(f(5, 3))


# 2
f = lambda x: "Fizz" if x % 3 == 0 else x
print(f(9))


# 3
f = lambda x: "OK" if x % 2 == 0 and x % 3 == 0 else "NO"
print(f(6))


# 4
f = lambda x: "nol" if x == 0 else "yo'q nol"
print(f(0))


# 5
f = lambda x: "Range" if 1 <= x <= 10 else "Out"
print(f(7))


# 6
f = lambda a, b: (a + b) > 50
print(f(30, 25))


# 7
f = lambda x: "Good" if x % 2 == 0 and x > 0 else "Bad"
print(f(4))


# 8
f = lambda x: x**2 if x % 4 == 0 else x**3
print(f(8))


# 9
f = lambda x: x if x >= 10 else 10
print(f(6))


# 10
f = lambda a, b: a if a == b else (a + b) / 2
print(f(5, 5))
