try:
    int("abc")
except Exception as e:
    print("Exception caught:")
    print(type(e), e)
