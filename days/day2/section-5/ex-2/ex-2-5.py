import tempfile

with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp:
    temp.write("Temporary content")
    temp.seek(0)
    print("Read from temp file:", temp.read())
