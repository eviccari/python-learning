items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


def get_price(item_list):
    return item_list[1]


x = map(get_price, items)
print(x)

prices = list(map(lambda item: item[1], items))
print(prices)
