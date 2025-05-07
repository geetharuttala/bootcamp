def read_lines(filepath):
    with open(filepath, "r") as f:
        for line in f:
            yield line.strip()

# Example usage
for line in read_lines("large_file.txt"):
    print(line)
    break  # print first line