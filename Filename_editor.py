import os

directory = ''  # Paste Here the path to the directory

common_part = ''  # Paste here tha part you want to remove

for filename in os.listdir(directory):
    if common_part in filename:
        prefix, sufix = filename.split(common_part, 1)

        new_name = prefix + sufix

        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)

        os.rename(old_path, new_path)
