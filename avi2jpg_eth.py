#!/usr/bin/python
# vim: set fileencoding=utf-8 :
############################################
#haochen.wang
#2018.01.23
############################################
import multiprocessing
import time
# import pylab
import imageio
import skimage
from PIL import Image
import os

video_path = ['seq_hotel/seq_hotel.avi','seq_eth/seq_eth.avi']
for video in video_path:
    vid = imageio.get_reader(video,  'ffmpeg')
    save_path = video.split('/')[0]+'/'+video.split('/')[0]
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    for i, img in enumerate(vid):
                    opencvImg = skimage.img_as_ubyte(img, True)
                    # 下边就回到熟悉的opencv套路上了
                    img = Image.fromarray(opencvImg)
                    img.save(save_path+'/'+str(i).zfill(6)+'.jpg')
                    if i%1000 == 0:
                        print('now its'+str(i)+'frame')
    
