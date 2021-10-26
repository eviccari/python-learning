letters = ["a", "b", "c", "d", "e", "f", "g"]

# Add
letters.append("d")
print(letters)

letters.insert(0, "-")
print(letters)

# Remove
letters.pop()
print(letters)

letters.pop(0)
print(letters)

letters.remove("c")
print(letters)

del letters[0:3]
print(letters)

letters.clear()
print(letters)