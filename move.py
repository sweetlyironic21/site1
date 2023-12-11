import os
import shutil
import random

def move_files(source_folder, destination_folder, num_files):
    # Get a list of all files in the source folder
    all_files = os.listdir(source_folder)
    
    # Randomly select 'num_files' files from the list
    selected_files = random.sample(all_files, num_files)
    
    # Move selected files to the destination folder
    for file_name in selected_files:
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.move(source_path, destination_path)
        print(f"Moved: {file_name}")

if __name__ == "__main__":
    # Specify the source and destination folders
    source_folder = "blog"
    destination_folder = "site3"
    
    # Specify the number of files to move
    num_files_to_move = 20000
    
    # Move files
    move_files(source_folder, destination_folder, num_files_to_move)
