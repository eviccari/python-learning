from ecommerce.shopping.sales import calc_shipping, calc_tax
from ecommerce.shopping import sales

calc_tax()  # type 1
calc_shipping()  # type 1

sales.calc_tax()  # type 2
sales.calc_shipping()  # type 2

print("finish")
