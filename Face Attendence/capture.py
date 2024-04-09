import cv2

cam_port = 0  # Adjust the camera port if needed
cam = cv2.VideoCapture(cam_port)

# Reading the input using the camera
inp = input('Enter person name: ')

# If image will detected without any error, show result
while True:
    ret, image = cam.read()
    cv2.imshow('Capture', image)
    key = cv2.waitKey(1)
    if key == ord('s'):  # Press 's' to save the image
        cv2.imwrite(inp + ".png", image)
        print("Image saved as", inp + ".png")
        break
    elif key == 27:  # Press 'Esc' to exit
        break

# Release the camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()