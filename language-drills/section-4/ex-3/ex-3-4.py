from functools import partial

print_info = partial(print, end=' ', flush=True)
print_warning = partial(print_info, "[WARNING]")
print_error = partial(print_info, "[ERROR]")

print_warning("Low disk space")
print_error("Failed to save file")
