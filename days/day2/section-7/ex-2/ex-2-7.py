def copy_file(source, dest):
    with open(source, "r") as src, open(dest, "w") as dst:
        for line in src:
            dst.write(line)

copy_file("source.txt", "copy.txt")
