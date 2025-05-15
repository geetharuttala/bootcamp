def echo():
    while True:
        value = yield
        print(f"Received: {value}")

gen = echo()
next(gen)
gen.send("Hello")