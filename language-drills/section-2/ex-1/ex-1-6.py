class Dynamic:
    def __getattr__(self, name):
        return f"{name} not found"

d = Dynamic()
print(d.missing)