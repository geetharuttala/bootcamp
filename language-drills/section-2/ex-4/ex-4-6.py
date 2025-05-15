import tempfile

with tempfile.TemporaryFile(mode="w+t") as tf:
    tf.write("Temporary content")
    tf.seek(0)
    print(tf.read())
