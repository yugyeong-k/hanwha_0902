# age = 36
# txt = f"age : {age}"
# print(txt)

# txt2 = f"age : {age:.2f}"
# print(txt2)

# txt3 = "banana"
# x = txt.center(20)
# print(x)

# txt4 = "Hello, welcome to my world."
# x2 = txt4.find("welcome")
# print(x2)

# txt5 = "THIS IS NOW!"
# x = txt5.isupper()
# print(x)

# txt6 = "     banana     "
# x = txt6
# print("of all fruits", x, "is my favorite")

# x = txt6.lstrip()
# print("of all fruits", x, "is my favorite")

# txt7 = "Hello Sam!"
# mytable = str.maketrans("S","P")
# print(txt7.translate(mytable))

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964
}

x = car.keys()
print(x)

car["color"] = "white"
print(x)

y = car.values()
print(y)

print(car)