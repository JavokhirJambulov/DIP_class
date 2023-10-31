import cv2

# Load your trained Haar Cascade classifier
cascade_path = 'D:/programming/custom haar cascade/cascade.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)

# Load a test image
image = cv2.imread('D:/programming/custom haar cascade/javokh_29.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define the range of sizes to test (e.g., from 20x20 to 300x300)
min_size = (20, 20)
max_size = (2000, 2000)

# Create an image pyramid to resize the test image for different sizes
for size in range(min_size[0], max_size[0] + 1, 20):
    resized_image = cv2.resize(gray, (size, size))
    faces = face_cascade.detectMultiScale(resized_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) > 0:
        print(f"Detected faces at size {size}x{size}")

cv2.waitKey(0)
cv2.destroyAllWindows()
