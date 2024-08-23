import math
import os
import cv2 as cv
import moviepy.editor as mp
# import subprocess as sp

if __name__ == '__main__':
    # GET FPS
    video = cv.VideoCapture(r"<PATH>\Downloads\sample.mp4")
    fps = math.ceil(video.get(cv.CAP_PROP_FPS))
    height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
    width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))

    # CROP VIDEO IF NEEDED
    if height != width:
        fourcc = cv.VideoWriter_fourcc(*'mp4v')
        out = cv.VideoWriter('result.mp4', fourcc, fps,
                             (height if height < width else width, height if height < width else width))
        while video.isOpened():
            ret, frame = video.read()
            if ret:
                if width > height:
                    crop = frame[0:height,
                           math.ceil((width - height) / 2):math.ceil(((width - height) / 2) + int(height))]
                else:
                    crop = frame[0:width,
                           math.ceil((height - width) / 2):math.ceil(((height - width) / 2) + int(width))]
                out.write(crop)

                if cv.waitKey(0) == 27:
                    exit(0)
            else:
                break
        video.release()
        out.release()
        video = cv.VideoCapture(r"<PATH>\PycharmProjects\hologramProject\result.mp4")
        height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
        width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))

    # DOWNSCALE IF NOT 512X512
    if not height == width == 256:
        clip = mp.VideoFileClip("result.mp4")
        clip_resized = clip.resize(height=512)
        clip_resized.write_videofile("resized.mp4")
        video = cv.VideoCapture(r"<PATH>\PycharmProjects\hologramProject\resized.mp4")
        height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
        width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))

    # GET FRAME JPGS (1 FRAME EVERY INTERVAL=FPS/2) -> 2 FRAMES / SECOND
    i = 0
    path = '<PATH>/PycharmProjects/hologramProject/sampled'
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break
        if i % (fps / 2) == 0:
            cv.imwrite(os.path.join(path, 'frame' + str(i) + '.jpg'), frame)
        i += 1
    video.release()
    cv.destroyAllWindows()

    # CREATE 3D OBJECTS
    i = 0
    sampled = '<PATH>/PycharmProjects/hologramProject/sampled'
    pifuhd = "<PATH>/Documents/Uni/Bachelor Sem/pifuhd-master"
    objects = "<PATH>/PycharmProjects/hologramProject/objects"
    while any(os.listdir(sampled)):
        os.remove(pifuhd+'/sample_images/test.jpg')
        os.rename(
            sampled+"/frame"+str(i)+".jpg",
            pifuhd+'/sample_images/test.jpg')
        # commands = 'conda init cmd.exe | conda activate pifuhd | python -m apps.simple_test'
        cwd = os.getcwd()
        os.chdir(pifuhd)
        # p = sp.check_output(commands, shell=True)
        os.system('cmd /c "conda init cmd.exe & conda activate pifuhd & python -m apps.simple_test"')
        os.chdir(cwd)
        # print(p.decode())
        os.rename(pifuhd+"/results/pifuhd_final/recon/result_test_256.obj",
                  objects+"/obj" + str(i) + ".obj")
        os.remove(pifuhd+"/results/pifuhd_final/recon/result_test_256.png")
        i += fps/2
