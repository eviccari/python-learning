import sys

if len(sys.argv) == 1:
    print("USAGE: python3 app.py <password>")
else:
    print("Password", sys.argv[1])
