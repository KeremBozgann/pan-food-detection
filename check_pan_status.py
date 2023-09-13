import cv2
import numpy as np

def check_hotel_pan_status_from_frame(image, image_green):
    threshold_full = 800000
    threshold_half_full = 900000


    lower_gray = (100, 100, 100)  # Adjust these values to match your gray shade
    upper_gray = (200, 200, 200)  # Adjust these values to match your gray shade

    mask = cv2.inRange(image, lower_gray, upper_gray)
    mask2 = cv2.inRange(image_green, lower_gray, upper_gray)
    gray_pixel_count = cv2.countNonZero(mask)
    gray_pixel_count_green = cv2.countNonZero(mask2)
    print(f'gray image, gray pixel count: {gray_pixel_count};'
          f' green image, gray pixel count: {gray_pixel_count_green}')


    if gray_pixel_count < threshold_full:
        print("The hotel pan is full")
        status = 'full'
    elif threshold_full <= gray_pixel_count < threshold_half_full:
        print("The hotel pan is partially full.")
        status = 'half full'
    else:
        print("The hotel pan is empty.")
        status = 'empty'

    return status



def check_hotel_pan_status_from_frame_prototype(image_green):
    threshold_full = 1000
    threshold_half_full = 500

    #dark green  of the plate
    dark_green_rgb = (120, 173, 144)
    hsv_color = cv2.cvtColor(np.uint8([[dark_green_rgb]]), cv2.COLOR_RGB2HSV)[0][0]
    hue, saturation, value = hsv_color
    print(f"Hue: {hue}, Saturation: {saturation}, Value: {value}")

    diff_hue = 10; diff_sat = 20; diff_val = 20;
    hue_lower = hue - diff_hue; hue_upper = hue+ diff_hue;
    saturation_lower = saturation - diff_sat ; saturation_upper = saturation + diff_sat ;
    value_lower = value -diff_val; value_upper = value + diff_val



    lower_bound = np.array([hue_lower, saturation_lower, value_lower])
    upper_bound = np.array([hue_upper, saturation_upper, value_upper])

    hsv_image = cv2.cvtColor(image_green, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
    green_pixel_count = cv2.countNonZero(mask)
    print(f' green image, green pixel count: {green_pixel_count}')


    if green_pixel_count < threshold_full:
        print("The hotel pan is full")
        status = 'full'
    elif threshold_full <= green_pixel_count < threshold_half_full:
        print("The hotel pan is partially full.")
        status = 'half full'
    else:
        print("The hotel pan is empty.")
        status = 'empty'

    return status



def check_hotel_pan_status_from_path(image_path_gray, image_path_green):
    threshold_empty = 5000
    threshold_half_full = 15000

    image = cv2.imread(image_path_gray)
    image_green = cv2.imread(image_path_green)


    lower_gray = (100, 100, 100)  # Adjust these values to match your gray shade
    upper_gray = (200, 200, 200)  # Adjust these values to match your gray shade

    mask = cv2.inRange(image, lower_gray, upper_gray)
    mask2 = cv2.inRange(image_green, lower_gray, upper_gray)
    gray_pixel_count = cv2.countNonZero(mask)
    gray_pixel_count_green = cv2.countNonZero(mask2)
    print(f'gray image, gray pixel count: {gray_pixel_count};'
          f' green image, gray pixel count: {gray_pixel_count_green}')


    if gray_pixel_count < threshold_empty:
        print("The hotel pan is full")
        status = 'full'
    elif threshold_empty <= gray_pixel_count < threshold_half_full:
        print("The hotel pan is partially full.")
        status = 'half full'
    else:
        print("The hotel pan is empty.")
        status = 'empty'

    return status

def test():
    image_path_gray  ='test.jpg'
    image_path_green  ='test_green.jpg'
    check_hotel_pan_status(image_path_gray, image_path_green)



