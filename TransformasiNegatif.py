import cv2

img = cv2.imread("Boruto.jpg", 0)

img_1 = 255 - img

cv2.imshow("Original Frame", img)
cv2.imshow("Image Negative", img_1)

cv2.waitKey(0)
cv2.destroyAllWindow()