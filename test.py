import time
import datetime
import os
import multiprocessing as mp

num_processes = 5

cams = ['121171', '101539', '101669', '101670', '101716']

def task(path):
    cmd = '/home/llubuntu/Documents/lisa_tools/gen_dgp.sh' + ' ' + path
    os.system(cmd)
def func(args):
    return task(*args)
while True:
    job_args = []
    if datetime.datetime.now().minute % 5 == 0 and datetime.datetime.now().second is 0:
        folder = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        time.sleep(60)
        for cam in cams:
            path = '/mnt/nas/LDR_Pictures/RICOH_ThetaV_2.50.1_00' + cam

            if os.path.exists(path + '/' + folder):
                job_args.append(path)
            pool = mp.Pool(processes=num_processes)
            pool.map(func, job_args)
            pool.close()
            pool.join()


