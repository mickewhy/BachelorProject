# Import OpenCV
import cv2 as cv
import math

# Define fps, height, and width of the video in provided path
video = cv.VideoCapture(r"<PATH>Downloads\sample.mp4")
fps = math.ceil(video.get(cv.CAP_PROP_FPS))
height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))

# If video is wider than it is high
if height != width:

    # Define preferred video codec
    fourcc = cv.VideoWriter_fourcc(*'mp4v')

    # Construct output video
    out = cv.VideoWriter('result.mp4', fourcc, fps,
    # Height and width should be equal since it is a square, pick the smallest of both values
                         (height if height < width else width, height if height < width else width))
    # While video isn't finished
    while video.isOpened():

        # Capture each frame
        ret, frame = video.read()

        # If a value is returned
        if ret:

            # If width is bigger than height
            if width > height:
                crop = frame[0:height,
                       math.ceil((width - height) / 2):math.ceil(((width - height) / 2) + int(height))]

            # If height is bigger than width
            else:
                crop = frame[0:width,
                       math.ceil((height - width) / 2):math.ceil(((height - width) / 2) + int(width))]

            # Write frame crop to output video 'out'
            out.write(crop)

            # Exit at any point with ESC
            if cv.waitKey(0) == 27:
                exit(0)
        else:
            break
    
    # Release both video objects
    video.release()
    out.release()

    # Redefine the new values for later use
    video = cv.VideoCapture(r"<PATH>PycharmProjects\hologramProject\result.mp4")
    height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
    width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))