items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

items.sort(key=lambda item: item[1])
#                      1    2
# 1: PARAMETERS
# 2: EXPRESSION

print(items)
