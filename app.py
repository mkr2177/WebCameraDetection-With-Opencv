import cv2
import time
import glob
import os
from send_email import send_email  # Make sure this function can send multiple images

# Initialize video capture
video = cv2.VideoCapture(0)
time.sleep(1)

image_count = 0
last_capture_time = time.time()
captured_images = []

def clean_folder():
    images = glob.glob("images/*.png")
    for image in images:
        os.remove(image)

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Show live video
    cv2.imshow("Live Video", frame)

    # Every 1 seconds, capture a frame
    current_time = time.time()
    if current_time - last_capture_time >= 1:
        image_path = f"images/image_{image_count + 1}.png"
        cv2.imwrite(image_path, frame)
        captured_images.append(image_path)
        image_count += 1
        last_capture_time = current_time
        print(f"Captured: {image_path}")

    # Press 'q' to quit and send email
    key = cv2.waitKey(1)
    if key == ord("q"):
        print("Quit key pressed.")
        break

# Clean up
video.release()
cv2.destroyAllWindows()

# Send captured images via email (if any)
if captured_images:
    print("Sending email with captured images...")
    send_email(captured_images)  # Your emailing.py must accept list
    clean_folder()
    print("Email sent and folder cleaned.")
else:
    print("No images captured to send.")
