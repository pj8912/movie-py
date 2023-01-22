from vidpy import Clip, Composition

# load the video
video = Clip("input.mp4")

# set the aspect ratio to 9:16
video.resize(h=900, w=506)

# set the position to (547, 0)
video.position(547, 0)

# create a composition and add the video
comp = Composition([video])

# save the new video
comp.save("new_video.mp4")
