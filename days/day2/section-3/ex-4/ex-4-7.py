from collections import namedtuple

# Invalid field names, will be renamed automatically if rename=True
Data = namedtuple("Data", ["class", "def"], rename=True)
d = Data(1, 2)
print(d)
print(d._0, d._1)
