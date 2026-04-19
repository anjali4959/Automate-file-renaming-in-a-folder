import os

# Path of the folder (change this to your folder path)
folder_path = "your_folder_path_here"

# Get list of files
files = os.listdir(folder_path)

# Counter for naming
count = 1

for file in files:
    old_path = os.path.join(folder_path, file)

    # Check if it's a file (not a folder)
    if os.path.isfile(old_path):
        # Get file extension
        ext = os.path.splitext(file)[1]

        # Create new file name
        new_name = f"file_{count}{ext}"
        new_path = os.path.join(folder_path, new_name)

        # Rename file
        os.rename(old_path, new_path)

        print(f"Renamed: {file} -> {new_name}")

        count += 1

print("All files renamed successfully!")

output:
Renamed: photo.png -> file_1.png
Renamed: document.pdf -> file_2.pdf
Renamed: notes.txt -> file_3.txt
Renamed: image.jpg -> file_4.jpg

All files renamed successfully!
