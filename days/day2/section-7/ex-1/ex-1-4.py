@profile
def heavy_function():
    result = 0
    for i in range(100000):
        result += i * i
    return result

if __name__ == "__main__":
    heavy_function()
