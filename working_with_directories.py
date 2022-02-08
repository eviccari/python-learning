from pathlib import Path

path = Path("ecommerce")

for p in path.iterdir():
    print(p)

paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)

py_files = [p for p in path.rglob("*.py")]  # recursive glob
print(py_files)

py_files = [p for p in path.glob("*.py")]  # searchs at root of ecommerce glob
print(py_files)
