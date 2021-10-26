letters = ["a", "b", "c"]

print(letters.index("a"))

if letters.count("d") > 0:
    letters.remove("d")

if "d" in letters:
    letters.remove("d")

print(letters.index("d"))  # should throw an error

print("end")
