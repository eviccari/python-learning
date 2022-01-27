from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    #print(error)
    pass
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    else:
        return 10 / age

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass  
else:
    print(xfactor)          
"""

print('Code with exception...: ', timeit(code1, number=1_000_000))
print('Code without exception: ', timeit(code2, number=1_000_000))


