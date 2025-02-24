import os
import shutil

# 1.
def list_contents(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    all_contents = os.listdir(path)

    print("Directories:", directories)
    print("Files:", files)
    print("All contents:", all_contents)

list_contents(".")  


# 2.
def check_access(path):
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

check_access(".")


# 3.
def path_info(path):
    if os.path.exists(path):
        print("Path exists")
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print("Path does not exist")

path_info("example.txt")


# 4.
def count_lines(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        print(f"Number of lines in {file_path}:", len(lines))

# Uncomment to test with an actual file
# count_lines("example.txt")


# 5.
def write_list_to_file(file_path, data_list):
    with open(file_path, "w") as file:
        for item in data_list:
            file.write(str(item) + "\n")

write_list_to_file("output.txt", ["Apple", "Banana", "Cherry"])


# 6.
def generate_files():
    for letter in range(65, 91):  # ASCII values for A-Z
        with open(f"{chr(letter)}.txt", "w") as file:
            file.write(f"This is {chr(letter)}.txt")

generate_files()


# 7.
def copy_file(source, destination):
    shutil.copy(source, destination)
    print(f"Copied contents from {source} to {destination}")


# 8.
def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            os.remove(file_path)
            print(f"Deleted file: {file_path}")
        else:
            print("No write access to delete the file.")
    else:
        print("File does not exist.")
