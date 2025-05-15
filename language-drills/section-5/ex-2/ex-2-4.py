import os
import shutil
import tempfile

with tempfile.TemporaryDirectory() as temp_dir:
    path = os.path.join(temp_dir, "demo_folder")
    os.makedirs(path)
    print("Created:", path)
    shutil.rmtree(path)
    print("Deleted:", path)
