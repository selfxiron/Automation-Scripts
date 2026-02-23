import os
import zipfile
import shutil
import glob

# Script to extract and rename files from zip archives
for zip_file in glob.glob('zipped-files/*.zip'):
    number = os.path.basename(zip_file)[:-4]  # Remove .zip extension
    temp_dir = f"temp_{number}"
    
    # Extract the zip file to a temporary directory
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)
    
    # Path to the source file inside the extracted folder
    source_file = os.path.join(temp_dir, "annotations", "instances_default.json")
    
    if os.path.exists(source_file):
        # Rename and move to the output-jsons directory
        dest_file = os.path.join("output-jsons", f"{number}.json")
        shutil.move(source_file, dest_file)
        print(f"Renamed and moved {source_file} to {dest_file}")
    else:
        print(f"File not found: {source_file}")
    
    # Clean up the temporary directory
    shutil.rmtree(temp_dir)