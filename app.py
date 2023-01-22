from moviepy.editor import VideoFileClip

# Open the video file
video = VideoFileClip("input.mp4")

# Set the frame rate of the video to 9/16
video = video.set_fps(video.fps * (9/16))

# Resize the video to 506x900
video = video.resize(width=506, height=900)

# Set the position of the video to (547, 0)
video = video.set_pos((547, 0))


video.write_videofile("output.mp4")






