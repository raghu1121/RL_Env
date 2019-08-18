import multiprocessing as mp
import csv
import os
import itertools

num_processes = mp.cpu_count()
processes = []
viewtimes = []
states = []
job_args = []
views = ['v1', 'v2', 'v3', 'v4']

with open('Potsdam.wea', 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    for item in itertools.islice(reader, 6, None):
        viewtimes.append(item)


list = ['8905', '8906', '8908', '8909']
for subset in itertools.product(list, repeat=3):
    states.append(subset)


def gendaylit(m, d, h, dir, diff):
    line = '!gendaylit' + ' ' + m + ' ' + d + ' ' + h + '  -m -15 -o -13.07 -a 52.38 -O 0 -W ' + dir + ' ' + diff
    sky_fname = path('sky', '', m, d) + '/sky_' + '_' + m + '_' + d + '_' + h + '.rad'
    if not os.path.isfile(sky_fname):
        with open('sky.rad', 'r') as infile, open(sky_fname, 'w') as outfile:
            outfile.write(line)
            outfile.write('\n')
            for item in itertools.islice(infile, 2, None):
                outfile.write(item)


def genECHDR(m, d, h, view, state):
    zone1 = state[0]
    zone2 = state[1]
    zone3 = state[2]
    # print(zone1,zone2,zone3)
    octree_fname = path('octree', '',  m,d) + '/' + m + '_' + d + '_' + h + '_' + zone1 + '_' + zone2 + '_' + zone3 + '.oct'
    hdr_fname = path('hdrs', view,  m,
                     d) + '/' + view + '_'+ m + '_' + d + '_' + h + '_' + zone1 + '_' + zone2 + '_' + zone3 + '.hdr'
    if not os.path.isfile(octree_fname):
        octree = 'oconv materials/materials.rad ' + path('sky', '',  m,
                                                         d) + '/sky_' +  '_' + m + '_' + d + '_' + h + '.rad Geometry/EC/EC_Bottom_' + zone3 + '.rad Geometry/EC/EC_Middle_' + zone2 + '.rad Geometry/EC/EC_Top_' + zone1 + '.rad Geometry/LiSA_ShoeBox.rad >  ' + octree_fname
        os.system(octree)
    if not os.path.isfile(hdr_fname):
        rpict = 'rpict -vf views/' + view + '.vf -x 800 -y 800 -vv 180 -vh 180 -ab 4  ' + octree_fname + ' > ' + hdr_fname
        os.system(rpict)


def path(folder, view,  month, day):
    try:
        os.makedirs(os.path.join(folder, view,  month, day))
    except OSError:
        pass
    return os.path.join(folder, view,  month, day)


def taskEC(viewtime, state, view):
    m = str(viewtime[0])
    d = str(viewtime[1])
    h = str(round(float(viewtime[2]), 2))
    dir = str(viewtime[3])
    diff = str(viewtime[4])
    view = view

    if (int(diff) > 0):
        gendaylit(m, d, h, dir, diff)

        genECHDR(m, d, h, view, state)


def func(args):
    return taskEC(*args)


pool = mp.Pool(processes=num_processes)
for viewtime in viewtimes:
    for state in states:
        for view in views:
            comb = [viewtime, state, view]
            job_args.append(comb)
pool.map(func, job_args)
pool.close()
pool.join()
