import streamlit as st
from PIL import Image
import numpy as np
from src.detection_libs.image_object_detection import detect_in_image  # Import the function for image inference
# from src.detection_libs.video_object_detection import detect_in_video  # Import the function for video inference
from src.detection_libs.yolov8 import YOLOv8

model_path = "src/models/model_ver1.onnx"
yolov8_detector = YOLOv8(model_path, conf_thres=0.2, iou_thres=0.3)

def main():
    st.title("Autonomous Helmet Detection App")

    # st.sidebar.header("Options")
    # option = st.sidebar.selectbox("Choose Input Type", ("Image"))

    # if option == "Image":
    st.subheader("Object Detection on Image")
    uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Display the original image
        st.subheader("Original Image")
        input_image = Image.open(uploaded_image)
        st.image(input_image, caption='Original Image', use_column_width=True)

        input_image = np.array(input_image)
        # Perform object detection on the image
        output_image = detect_in_image(input_image, yolov8_detector)

        # Display the inferenced image
        st.subheader("Inferenced Image")
        st.image(output_image, caption='Inferenced Image', use_column_width=True)

    # elif option == "Video":
    #     st.subheader("Object Detection on Video")
    #     uploaded_video = st.file_uploader("Upload Video", type=["mp4"])

    #     if uploaded_video is not None:
    #         # Get the video file path
    #         video_path = save_uploaded_video(uploaded_video)

    #         # Perform object detection on the video
    #         output_video_path = detect_in_video(video_path, yolov8_detector)

    #         # Display the original and inferenced videos side by side
    #         st.subheader("Original Video")
    #         st.video(video_path)

    #         st.subheader("Inferenced Video")
    #         st.video(output_video_path)


# def save_uploaded_video(uploaded_video):
#     # Save the uploaded video to a temporary location
#     with open("temp_video.mp4", "wb") as f:
#         f.write(uploaded_video.getbuffer())
#     return "temp_video.mp4"


if __name__ == '__main__':
    main()
