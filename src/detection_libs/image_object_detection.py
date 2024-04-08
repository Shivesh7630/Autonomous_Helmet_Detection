# Read image
# Detect Objects
def detect_in_image(img, yolov8_detector):
    # Initialize yolov8 object detector
    boxes, scores, class_ids = yolov8_detector(img)

    # Draw detections
    combined_img = yolov8_detector.draw_detections(img)
    
    return combined_img
    # cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
    # cv2.imshow("Detected Objects", combined_img)
    # cv2.imwrite("doc/img/detected_objects.jpg", combined_img)
    # cv2.waitKey(0)
