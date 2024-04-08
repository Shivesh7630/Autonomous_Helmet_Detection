import os
import argparse

def scale_bbox_coordinates(bbox, original_width, original_height, target_width, target_height):
    x, y, w, h = bbox
    x_scaled = x * (target_width / original_width)
    y_scaled = y * (target_height / original_height)
    w_scaled = w * (target_width / original_width)
    h_scaled = h * (target_height / original_height)
    return x_scaled, y_scaled, w_scaled, h_scaled

def update_labels(source_folder, original_width, original_height, target_width, target_height):
    """
    Update label files in the source folder by scaling the bounding box coordinates.

    Args:
    source_folder (str): Path to the folder containing label files.
    original_width (int): Original width of the images.
    original_height (int): Original height of the images.
    target_width (int): Target width of the images.
    target_height (int): Target height of the images.
    """
    # Iterate through files in the source folder
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        # Check if it's a file and ends with .txt extension
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            # Read the content of the label file
            with open(file_path, 'r') as file:
                lines = file.readlines()
            # Scale the bounding box coordinates
            scaled_lines = []
            for line in lines:
                parts = line.strip().split(' ')
                bbox = tuple(map(float, parts[1:]))
                scaled_bbox = scale_bbox_coordinates(bbox, original_width, original_height, target_width, target_height)
                scaled_line = ' '.join([parts[0]] + [f'{coord:.6f}' for coord in scaled_bbox]) + '\n'
                scaled_lines.append(scaled_line)
            # Write the updated content back to the label file
            with open(file_path, 'w') as file:
                file.writelines(scaled_lines)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Update label files by scaling the bounding box coordinates.')
    parser.add_argument('source_folder', type=str, help='Path to the folder containing label files.')
    # parser.add_argument('--original_width', type=int, default=1280, help='Original width of the images.')
    # parser.add_argument('--original_height', type=int, default=720, help='Original height of the images.')
    # parser.add_argument('--target_width', type=int, default=640, help='Target width of the images.')
    # parser.add_argument('--target_height', type=int, default=360, help='Target height of the images.')
    args = parser.parse_args()

    # Call the function
    update_labels(args.source_folder, 1280, 720, 1280, 720)
