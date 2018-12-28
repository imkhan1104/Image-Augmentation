# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 15:18:37 2018

@author: imrankhan
"""

import os
import cv2
from PIL import Image

img_dir = "C:/Users/imrankhan/MAXIS/sample_img/"

for fp in os.listdir(img_dir):
    img = [Image.open(img_dir+fp)]
    
    for j, image, in enumerate(img):
    
        width = image.size[0]
        height = image.size[1]
    
        print("image "+str(fp)+" started")  
        
        f = fp[:-4]
        
        cropped1 = image.crop((0, 0, width/2, height/2))
        cropped2 = image.crop((0, height/2, width/2, height))
        cropped3 = image.crop((width/2, 0, width, height/2))
        cropped4 = image.crop((width/2, height/2, width, height))
        cropped5 = image.crop((width/4, height/4, (3*width)/4, (3*height)/4))
        cropped6 = image.crop((width/4, 0, (3*width)/4, height/2))
        cropped7 = image.crop((0, height/4, width/2, (3*height)/4))
        cropped8 = image.crop((width/4, height/2,(3*width)/4, height))
        cropped9 = image.crop((width/2, height/4, width, (3*height)/4))
        
        
        cropped1.save(os.getcwd() + "/output/" + f + "_Crop_1.jpg")
        cropped2.save(os.getcwd() + "/output/" + f + "_Crop_2.jpg")
        cropped3.save(os.getcwd() + "/output/" + f + "_Crop_3.jpg")
        cropped4.save(os.getcwd() + "/output/" + f + "_Crop_4.jpg")
        cropped5.save(os.getcwd() + "/output/" + f + "_Crop_5.jpg")
        cropped6.save(os.getcwd() + "/output/" + f + "_Crop_6.jpg")
        cropped7.save(os.getcwd() + "/output/" + f + "_Crop_7.jpg")
        cropped8.save(os.getcwd() + "/output/" + f + "_Crop_8.jpg")
        cropped9.save(os.getcwd() + "/output/" + f + "_Crop_9.jpg")
        
        
        print("image saved")
        cv2.waitKey(20)
    