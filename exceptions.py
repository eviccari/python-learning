try:
    file = open()
    age = int(input("Age:"))
    age = age / 0
except (ValueError, ZeroDivisionError) as error:
    print("You didn't enter a valid age")
    print(error)
    print(type(error))
else:
    print("No problem on the process")
