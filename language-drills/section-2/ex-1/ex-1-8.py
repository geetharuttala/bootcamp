def shout(text):
    if isinstance(text, str):
        print(text.upper())
    else:
        print("Not a string")

shout("hello")
shout(123)
