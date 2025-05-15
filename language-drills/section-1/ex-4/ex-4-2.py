def outer():
    msg = "Hello from outer"

    def inner():
        print(msg)
    inner()

outer()
