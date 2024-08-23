# Import libraries
import os

# Empty counter
i = 0

# Main folders' paths
sampled = '<PATH>/PycharmProjects/hologramProject/sampled'
pifuhd = "<PATH>/Documents/Uni/Bachelor Sem/pifuhd-master"
objects = "<PATH>/PycharmProjects/hologramProject/objects"

# While any file is still in the 'sampled' folder
while any(os.listdir(sampled)):

    # Remove the previous testing image used in PIFuHD
    os.remove(pifuhd+'/sample_images/test.jpg')
    # Move frame(i).jpg into PIFuHD as the testing image
    os.rename(sampled+"/frame"+str(i)+".jpg", pifuhd+'/sample_images/test.jpg')

    # Get current working directory and save in cwd
    cwd = os.getcwd()
    # Set current directory to the 'pifuhd' folder
    os.chdir(pifuhd)

    # Run the shell commands in the string seperated by '&'
    os.system('cmd /c "conda init cmd.exe & conda activate pifuhd & python -m apps.simple_test"')

    # Redirect to the original working directory
    os.chdir(cwd)

    # Move object result into 'objects' folder with the new name object(i).obj
    os.rename(pifuhd+"/results/pifuhd_final/recon/result_test_256.obj", objects+"/obj" + str(i) + ".obj")
    # Delete mesh image
    os.remove(pifuhd+"/results/pifuhd_final/recon/result_test_256.png")

    # Increment naming counter
    i += 15