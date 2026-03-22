import cv2

image = cv2.imread('example.jpg')

if image is None:
    print("Error: Image not found")
    exit()

h, w = image.shape[:2]

y = h // 2

cv2.arrowedLine(image, (10, y), (w-10, y), (0, 255, 0), 2, tipLength=0.05)
cv2.arrowedLine(image, (w-10, y), (10, y), (0, 255, 0), 2, tipLength=0.05)

text = f"Width: {w} pixels"
cv2.putText(image, text, (20, y - 20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

cv2.imshow("Annotated Image", image)
cv2.imwrite("annotated_width.jpg", image)

cv2.waitKey(0)
cv2.destroyAllWindows()