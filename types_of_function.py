def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Henrique Viccari")
print(message)

file = open("messages.txt", "w")
file.write(message)
