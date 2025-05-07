from collections import defaultdict

nested = defaultdict(lambda: defaultdict(int))
nested['user1']['score'] += 10
nested['user2']['score'] += 5
print(dict(nested))
