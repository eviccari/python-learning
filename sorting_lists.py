# numbers = [3, 51, 2, 8, 6]
# numbers.sort()
# print(sorted(numbers))
# print(sorted(numbers, reverse=True))
# print(numbers)

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)
