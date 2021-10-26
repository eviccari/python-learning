message = "a"


def greet(name):
    global message
    message = "b"


greet("Henrique")
print(message)
