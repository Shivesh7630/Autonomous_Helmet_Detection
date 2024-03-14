import os
import argparse

def update_labels(source_folder):
    """
    Update label files in the source folder by replacing occurrences of '15' with '0' and '16' with '1'.

    Args:
    source_folder (str): Path to the folder containing label files.
    """
    # Iterate through files in the source folder
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        # Check if it's a file and ends with .txt extension
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            # Read the content of the label file
            with open(file_path, 'r') as file:
                content = file.read()
            # Replace occurrences of '15' with '0' and '16' with '1'
            content = content.replace('15', '0').replace('16', '1')
            # Write the updated content back to the label file
            with open(file_path, 'w') as file:
                file.write(content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Update label files by replacing 15 with 0 and 16 with 1.')
    parser.add_argument('source_folder', type=str, help='Path to the folder containing label files.')
    args = parser.parse_args()

    # Call the function
    update_labels(args.source_folder)
