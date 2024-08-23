import os

if __name__ == '__main__':
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
        i += 4
