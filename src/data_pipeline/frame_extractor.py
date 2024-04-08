import cv2
import os
import sys

def extract_images(video_path, output_folder, frame_interval=1, image_prefix="frame"):
    """
    Extract frames from a video at specified intervals.

    Parameters:
        video_path (str): Path to the input video file.
        output_folder (str): Path to the folder where extracted images will be saved.
        frame_interval (int): Interval between extracted frames. Default is 1 (every frame).
        image_prefix (str): Prefix to be included in every image name.
    """
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)
    
    # Check if the video file was opened successfully
    if not video_capture.isOpened():
        print("Error: Unable to open video file.")
        return
    
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Initialize variables
    frame_count = 0
    
    # Loop through the video frames
    while True:
        # Read a frame from the video
        ret, frame = video_capture.read()
        
        # Check if frame reading was successful
        if not ret:
            break
        
        # Check if it's time to extract a frame based on frame_interval
        if frame_count % frame_interval == 0:
            # Construct the output file path
            output_file = os.path.join(output_folder, f"{image_prefix}_{frame_count}.jpg")
            
            # Save the extracted frame as an image file
            cv2.imwrite(output_file, frame)
            
            # Print progress
            print(f"Frame {frame_count} saved as {output_file}")
        
        # Increment frame count
        frame_count += 1
    
    # Release the video capture object
    video_capture.release()
    print("Extraction complete.")

if __name__ == "__main__":
    # Check if correct number of command line arguments are provided
    if len(sys.argv) < 2:
        print("Usage: python frame_extractor.py <video_path> [<image_prefix>]")
        sys.exit(1)
    
    # Extract command line arguments
    video_path = sys.argv[1]
    image_prefix = sys.argv[2] if len(sys.argv) > 2 else "frame"
    
    # Set the output folder
    output_folder = "Raw_Data"
    
    # Extract images
    extract_images(video_path, output_folder, image_prefix = image_prefix)
