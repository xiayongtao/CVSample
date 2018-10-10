import cv2


cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('Test camera')
success, frame = cameraCapture.read()
while success:
    if cv2.waitKey(1) == 27:
        break
    cv2.imshow('Test camera', frame)
    success, frame = cameraCapture.read()

cameraCapture.release()
