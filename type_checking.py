
from typing import List

container : List[int] = []

container.append(1)
container.append(1.0)
container.append("adsad")
print(container)

# python type_checking.py works fine
# mypy type_checking will give you incompatible types

