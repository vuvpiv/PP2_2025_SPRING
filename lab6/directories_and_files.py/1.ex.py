
import os

path = r"/Users/aidan/Desktop"

if os.path.exists(path):
    all_items = os.listdir(path)
    directories = [d for d in all_items if os.path.isdir(os.path.join(path, d))]
    files = [f for f in all_items if os.path.isfile(os.path.join(path, f))]
    print("\nOnly Directories:")
    print(directories)
    print("\nOnly Files:")
    print(files)
    print("\nAll Files and Directories:")
    print(all_items)
else:
    print("The specified path does not exist.")
