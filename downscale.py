# Import libraries
import cv2 as cv
import moviepy.editor as mp

# If height and width aren't equal to 512
if not height == width == 512:

    # Load cropped result.mp4 into mp
    clip = mp.VideoFileClip("result.mp4")

    # Resize and save
    clip_resized = clip.resize(height=512)
    clip_resized.write_videofile("resized.mp4")

    # Redefine video parameters for later use
    video = cv.VideoCapture(r"<PATH>\PycharmProjects\hologramProject\resized.mp4")
    height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
    width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))