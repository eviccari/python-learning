import random
import string

print(random.random())
print(random.randint(1, 20))
print(random.choice([1, 2, 3, 4, 5]))
print(random.choices([1, 2, 3, 4, 5], k=2))

print(string.punctuation)
print(random.choices(string.ascii_letters + string.digits, k=10))
print(
    "".join(
        random.choices(
            string.ascii_letters + string.digits + string.punctuation,
            k=10,
        )
    )
)

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)
