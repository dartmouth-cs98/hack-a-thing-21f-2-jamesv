import cv2

img = cv2.imread("Resources/lena.png")

cv2.imshow("Lena", img)
cv2.waitKey(0)

frameWidth = 640
frameHeight = 480

# Could not find the resource video so commented out
"""
cap = cv2.VideoCapture("Resources/test_video.mp4")
while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Result", img)

    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
"""

# might need to run once to give permission and then run again
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
