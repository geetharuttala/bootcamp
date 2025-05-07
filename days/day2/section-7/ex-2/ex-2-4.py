big_list = range(1_000_000)

has_divisible = any(x % 99 == 0 for x in big_list)
print("Contains a number divisible by 99:", has_divisible)
