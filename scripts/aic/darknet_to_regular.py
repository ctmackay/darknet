import os
os.system('ls')
from itertools import izip

output_path = '/home/charles/Pictures/datasets/aic540/val/images'
darknet_val_set = '/home/charles/Pictures/datasets/scripts/aic540-darknet-val-images.txt'
mapping_set = '/home/charles/Pictures/datasets/aic540-darknet/val/mapping_bak.txt'
darknet_img_path = '/home/charles/Pictures/datasets/aic540-darknet/val/images/'

with open(darknet_val_set,'r') as drk_f, open(mapping_set,'r') as map_f:
    for d, m in izip(drk_f, map_f):
        print(d,m)
        drk_img = darknet_img_path + d.strip()

        print(drk_img)
        system_call = 'ln -s ' + str(drk_img) + " /home/charles/Pictures/datasets/aic540/val/images/" + str(m.strip())
        print system_call
        os.system(system_call)