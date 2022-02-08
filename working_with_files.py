from pathlib import Path
from time import ctime
import shutil

path = Path("ecommerce/__init__.py")
print(path.exists())
# path.rename("test.txt")
# path.unlink()
print(ctime(path.stat().st_ctime))
print(path.read_text())

source = Path("ecommerce/__init__.py")
target = Path("ecommerce/other_init.py")
shutil.copy(source, target)
