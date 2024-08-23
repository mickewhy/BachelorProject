# Import libraries
import cv2 as cv
import os

# Empty counter
i = 0

# Path for saving sampled images
path = '<PATH>/PycharmProjects/hologramProject/sampled'

# While video isn't finished
while video.isOpened():

    # Capture each frame
    ret, frame = video.read()

    # If return is false, video is over
    if not ret:
        break
    
    # Adjust condition of If for more or less sample images
    if i % (fps / 2) == 0:

        # Create new .jpg file with the name frame(i)
        cv.imwrite(os.path.join(path, 'frame' + str(i) + '.jpg'), frame)
    
    # Increment i after each loop
    i += 1

# Release video and destroy all windows
video.release()
cv.destroyAllWindows()