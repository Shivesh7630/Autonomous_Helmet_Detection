import os
import subprocess
import sys

def annotate_images(image_folder, labelimg_path):
    """
    Annotate images in a folder using LabelImg.

    Parameters:
        image_folder (str): Path to the folder containing images to be annotated.
        labelimg_path (str): Path to the LabelImg executable.
    """
    # Check if image folder exists
    if not os.path.exists(image_folder):
        print(f"Error: Image folder '{image_folder}' not found.")
        return
    
    # Check if LabelImg executable exists
    if not os.path.exists(labelimg_path):
        print(f"Error: LabelImg executable '{labelimg_path}' not found.")
        return
    
    # Get list of image files in the folder
    image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.JPG', '.JPEG', '.PNG', '.BMP'))]
    
    # Check if there are images to annotate
    if not image_files:
        print(f"No images found in '{image_folder}'.")
        return
    
    # Launch LabelImg for each image
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        subprocess.run(["python", labelimg_path, image_path])

if __name__ == "__main__":
    # Check if correct number of command line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python annotate_data.py <image_folder> <labelimg_path>")
        sys.exit(1)
    
    # Extract command line arguments
    image_folder = sys.argv[1]
    labelimg_path = sys.argv[2]
    
    # Annotate images
    annotate_images(image_folder, labelimg_path)
