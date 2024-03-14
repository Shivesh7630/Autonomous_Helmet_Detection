import os
import shutil
import argparse

def separate_images_and_labels(source_folder, image_folder, label_folder):
    """
    Move images and labels from a source folder to separate image and label folders.

    Args:
    source_folder (str): Path to the source folder containing both images and labels.
    image_folder (str): Path to the destination folder where images will be moved.
    label_folder (str): Path to the destination folder where labels will be moved.
    """
    # Create destination folders if they don't exist
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)
    if not os.path.exists(label_folder):
        os.makedirs(label_folder)

    # Iterate through files in the source folder
    for filename in os.listdir(source_folder):
        # Check if it's a file
        if os.path.isfile(os.path.join(source_folder, filename)):
            # Check file extension
            file_extension = filename.split('.')[-1].lower()
            if file_extension in ['jpg', 'jpeg', 'png', 'gif']:  # Adjust image extensions as needed
                shutil.move(os.path.join(source_folder, filename), os.path.join(image_folder, filename))
            elif file_extension in ['txt', 'csv', 'xml', 'json']:  # Adjust label extensions as needed
                shutil.move(os.path.join(source_folder, filename), os.path.join(label_folder, filename))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Separate images and labels into separate folders.')
    parser.add_argument('source_folder', type=str, help='Path to the source folder containing both images and labels.')
    parser.add_argument('image_folder', type=str, help='Path to the destination folder where images will be moved.')
    parser.add_argument('label_folder', type=str, help='Path to the destination folder where labels will be moved.')
    args = parser.parse_args()

    # Call the function
    separate_images_and_labels(args.source_folder, args.image_folder, args.label_folder)
