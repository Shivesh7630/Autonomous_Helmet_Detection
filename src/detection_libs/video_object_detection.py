# import cv2

# def detect_in_video(uploaded_video_path, yolov8_detector, start_time=0):
#     # Initialize video capture
#     cap = cv2.VideoCapture(uploaded_video_path)
#     cap.set(cv2.CAP_PROP_POS_FRAMES, start_time * cap.get(cv2.CAP_PROP_FPS))

#     # Output video writer
#     output_path = f"{uploaded_video_path}_inferenced.mp4"
#     out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), cap.get(cv2.CAP_PROP_FPS), 
#                           (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # Object detection
#         boxes, scores, class_ids = yolov8_detector(frame)
#         combined_img = yolov8_detector.draw_detections(frame)

#         out.write(combined_img)

#     # Release resources
#     cap.release()
#     out.release()

#     return output_path