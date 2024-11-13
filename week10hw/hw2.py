import cv2
import numpy as np
yellow_lower = np.array([20, 100, 100], dtype=np.uint8)
yellow_upper = np.array([30, 255, 255], dtype=np.uint8)
white_lower = np.array([0, 0, 200], dtype=np.uint8)
white_upper = np.array([180, 25, 255], dtype=np.uint8)
image_files = ["1.jpg", "2.jpg", "3.jpg", "4.jpg"]
for file in image_files:
 img = cv2.imread(file)
 img = cv2.resize(img, (640, 480))
 
 hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
 
 yellow_mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
 white_mask = cv2.inRange(hsv, white_lower, white_upper)
 
 combined_mask = cv2.bitwise_or(yellow_mask, white_mask)
 
 result = cv2.bitwise_and(img, img, mask=combined_mask)
 cv2.imshow("Yellow and White Lines", result)
 cv2.waitKey(0)
cv2.destroyAllWindows()
