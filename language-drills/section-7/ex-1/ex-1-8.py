from memory_profiler import profile

@profile
def use_memory():
    a = [i for i in range(100000)]
    return sum(a)

if __name__ == "__main__":
    use_memory()
