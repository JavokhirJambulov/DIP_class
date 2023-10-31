import cv2
import time

faceCascade = cv2.CascadeClassifier("D:/programming/custom haar cascade/cascade.xml")

video_capture = cv2.VideoCapture(0)

total_image_detection_time = 0
total_face_detection_time = 0
frame_count = 0
face_count = 0

while True:
    # Capture frame-by-frame and record the start time
    ret, frame = video_capture.read()
    start_time = time.time()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,
                                         scaleFactor=1.1,
                                         minNeighbors=8,
                                         minSize=(30, 30),
                                         flags=cv2.CASCADE_SCALE_IMAGE)

    # Record the time taken for face detection in this frame
    frame_detection_time = time.time() - start_time
    total_image_detection_time += frame_detection_time

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Record the time taken for each face detection
        total_face_detection_time += frame_detection_time
        face_count += 1

    frame_count += 1

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

# Calculate average detection times
average_image_detection_time = total_image_detection_time / frame_count
average_face_detection_time = total_face_detection_time / face_count

print("Average detection time per image: {:.10f} seconds".format(average_image_detection_time))
print("Average detection time per face: {:.10f} seconds".format(average_face_detection_time))
