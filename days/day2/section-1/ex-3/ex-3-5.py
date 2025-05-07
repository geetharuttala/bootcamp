def mixed_args(*args, **kwargs):
    print("Positional args:", args)
    print("Keyword args:", kwargs)

mixed_args(1, 2, mode="fast", debug=True)

