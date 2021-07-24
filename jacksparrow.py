import cv2

def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)

img = cv2.imread('c.jpeg')
cv2.imshow("Capitan",img)
cv2.waitKey(500)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Capitan",img_gray)
cv2.waitKey(500)
img_invert = cv2.bitwise_not(img_gray)
cv2.imshow("Capitan",img_invert)
cv2.waitKey(500)
img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),0)
cv2.imshow("Capitan",img_smoothing)
cv2.waitKey(500)
final_img = dodgeV2(img_gray, img_smoothing)
cv2.imshow("Capitan",final_img)
cv2.waitKey(2000)
