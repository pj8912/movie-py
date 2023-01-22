import cv2

# Load the video
cap = cv2.VideoCapture("input.mp4")

# Get the frames per second (fps) and frame size
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# Define the codec and create a video writer object
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("new_video.mp4", fourcc, fps, (506, 900))

# Loop through the frames of the original video
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize the frame to 506x900
    frame = cv2.resize(frame, (506, 900))

    # Crop the frame to 9:16 aspect ratio
    frame = frame[0:900, 547:1053]

    # Write the frame to the new video
    out.write(frame)

# Release the video writer and capture objects
cap.release()
out.release()

