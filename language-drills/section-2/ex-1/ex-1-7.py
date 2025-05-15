user_input = "abc"

try:
    val = int(user_input)
except ValueError:
    val = 0

print(val)