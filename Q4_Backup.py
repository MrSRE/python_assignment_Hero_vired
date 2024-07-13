import os
import shutil
import sys
import time
from datetime import datetime

def backup_files(source_dir, destination_dir):
    """
    Backup files from source directory to destination directory.

    Args:
    source_dir (str): The path to the source directory.
    destination_dir (str): The path to the destination directory.
    """
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    # Check if destination directory exists
    if not os.path.exists(destination_dir):
        print(f"Error: Destination directory '{destination_dir}' does not exist.")
        return

    # Ensure the destination directory exists
    os.makedirs(destination_dir, exist_ok=True)

    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        destination_file = os.path.join(destination_dir, filename)

        # If the destination file exists, append a timestamp to the file name
        if os.path.exists(destination_file):
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            destination_file = os.path.join(destination_dir, f"{filename}_{timestamp}")

        try:
            # Copy the file
            shutil.copy2(source_file, destination_file)
            print(f"Copied '{source_file}' to '{destination_file}'")
        except Exception as e:
            print(f"Error copying '{source_file}' to '{destination_file}': {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_dir> <destination_dir>")
        sys.exit(1)

    source_dir = sys.argv[1]
    destination_dir = sys.argv[2]

    backup_files(source_dir, destination_dir)
