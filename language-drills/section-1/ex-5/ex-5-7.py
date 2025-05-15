from contextlib import suppress

my_dict = {"a": 1}

with suppress(KeyError):
    print(my_dict["b"])