import cv2
image = cv2.imread("./f/1.png")

def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

cropped = image[10:500, 500:2000]
viewImage(cropped, "после кадрирования")
