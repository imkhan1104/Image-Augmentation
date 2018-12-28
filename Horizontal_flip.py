# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 17:10:36 2018

@author: IMRANKHAN
"""

import imgaug as ia
import imgaug.imgaug.augmenters as iaa
import glob
import os

import cv2
from scipy import misc




fps = glob.glob("C:/Users/imrankhan/MAXIS/buffer/DJI_*.jpg")

img = [cv2.imread(fp) for fp in fps]



pic_num= 469
for j, image in enumerate(img):
    
    b,g,r = cv2.split(image)   
    rgb_img = cv2.merge([r,g,b])
    
    seq = iaa.Fliplr(1.0)
 
    
    image_aug = seq.augment_images([rgb_img])[0]
    
        
    misc.imsave(os.getcwd()+"/done/DJI_" + str(pic_num).zfill(4) + "_Flip.jpg", image_aug) 
    pic_num+=1
    cv2.waitKey(20)
    
    
