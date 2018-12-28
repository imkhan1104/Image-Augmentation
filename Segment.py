# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 10:46:30 2018

@author: IMRANKHAN
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
        
        cropped1 = image.crop((0, 0, width/2, height))
        cropped2 = image.crop((width/2, 0, width, height))
        cropped3 = image.crop((width/4, 0, (3*width)/4, height))

        cropped1.save(os.getcwd() + "/output/" + f + "_Crop_1.jpg")
        cropped2.save(os.getcwd() + "/output/" + f + "_Crop_2.jpg")
        cropped3.save(os.getcwd() + "/output/" + f + "_Crop_3.jpg")
    
        print("image saved")
        cv2.waitKey(20)
    
    
        
    


    


 
