import cv2
import numpy as np
from check_pan_status import check_hotel_pan_status_from_frame_prototype
import time


# Initialize the camera (0 is usually the default camera, but it may vary)
cap = cv2.VideoCapture(0)

# Create a window for displaying the camera feed
cv2.namedWindow("Mac Camera", cv2.WINDOW_NORMAL)

# Create a window for displaying the tray status text
cv2.namedWindow("Tray Status", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Tray Status", 400, 100)


while True:
    # Capture a frame from the camera
    ret, frame = cap.read()
    frame_empty = np.zeros((480, 640, 3), dtype=np.uint8)

    if not ret:
        break

    # Call the function to check the hotel pan status
    plate_status = check_hotel_pan_status_from_frame_prototype(frame)

    # Display the result on the image window
    cv2.putText(frame, f"Hotel Pan: {plate_status}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("Mac Camera", frame)


    empty_color = (0, 0, 255)  # Red for empty, Green for full
    full_color = (0, 255, 0)
    status_text = "Empty" if plate_status == "empty" else "Full"
    if plate_status == 'empty':
        cv2.putText(frame_empty, f"Tray Status: {status_text}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, empty_color, 2)
    else:
        cv2.putText(frame_empty, f"Tray Status: {status_text}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, full_color, 2)

    cv2.imshow("Tray Status", frame_empty)




    time.sleep(0.5)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

