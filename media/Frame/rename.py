import os

# Define the directory path
directory = 'D:\Projects\TheDominicanCode_SPA\Domini-Xode\media\Frame\SOPHOMORE\\'

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the filename contains the digit "3"
    if '2' in filename:
        # Create the new filename by removing all instances of "3"
        new_filename = filename.replace('2', '')
        
        # Construct full file paths
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(old_file, new_file)
        
        # Print the old and new filenames for verification
        print(f'Renamed: {old_file} -> {new_file}')