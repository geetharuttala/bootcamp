from collections import defaultdict
from functools import partial

nested_dict = partial(defaultdict, dict)
d = nested_dict()
d['key1']['subkey'] = 'value'
print(d)