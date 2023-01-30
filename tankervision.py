import cv2
vid = cv2.VideoCapture(0)
while True:
    ret, image = vid.read()
    cv2.imshow("Motor Camera", image)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:    #Нажмите esc для завершения программы
        break
vid.release()
cv2.destroyAllWindows()
