from vidgear.gears import VideoGear
import cv2

video = VideoGear(source='input.mp4')

video.aspect_ratio = (9, 16)
video.position = (547, 0)
video.size = (506, 900)

#video.open()

while True:
    frame = video.read()
    if frame is None:
        break
    cv2.imshow("Output Frame", frame)
    #video.write(frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break


video.stop()
