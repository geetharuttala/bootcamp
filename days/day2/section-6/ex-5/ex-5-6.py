def calculate_total(prices):
    return sum(prices)

def calculate_average(prices):
    return calculate_total(prices) / len(prices)

prices = [10, 20, 30]
print(calculate_average(prices))
