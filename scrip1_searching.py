import os


path = r".\files"

for file in os.listdir(path):
    if not file.endswith(".gif"):
        if "project30" in file or "commercial" in file:
            print(file)
