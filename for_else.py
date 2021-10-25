successful = False

for number in range(3):
    print("Attempt", number)
    if successful:
        print("Attempt successful")
        break
else:
    print("Attempt 3 times and failed")
