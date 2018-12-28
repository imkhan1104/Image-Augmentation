# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 15:58:55 2018

@author: IMRANKHAN
"""

import os
import xml.etree.ElementTree as ET
import imgaug.imgaug.augmenters as iaa
import glob
import cv2
from scipy import misc


    
def ImageFlip (img_dir):
   
    fps = glob.glob(img_dir + "*.jpg")

    img = [cv2.imread(fp) for fp in fps]
    
    fname = os.path.basename(max(fps, key = os.path.getctime))[:-4]
    
    
    pic_num=1
    
    for j, image in enumerate(img):
    
        b,g,r = cv2.split(image)   
        rgb_img = cv2.merge([r,g,b])
    
        seq = iaa.Fliplr(1.0)
 
    
        image_aug = seq.augment_images([rgb_img])[0]
    
        
        misc.imsave(os.getcwd()+"/output/image_flip/" + fname + "_Flip.jpg", image_aug) 
        pic_num+=1
        cv2.waitKey(20)
    


def BndBoxFlip(xml_dir):
    
    
        def get_width (xml_dir):
                
            for i in root:
                w = root[4][0].text     
            
                return int(w)
    

        def get_NewXmax (old_xmin, width):
    
            return width - old_xmin

        def get_NewXmin (old_xmax, width):
       
            return width - old_xmax
    
    
        for a in os.listdir(xml_dir):
        
        
            with open(xml_dir+a, encoding="utf8") as f:    
                tree = ET.parse(f)
                root = tree.getroot()
                width = get_width(xml_dir)
                print(width)
        
            for b in root.findall(".//bndbox"):   
                newXmax = get_NewXmax(int(b[0].text),width)
                newXmin = get_NewXmin(int(b[2].text),width)
        
                b[0].text = str(newXmin)
                b[2].text = str(newXmax)
            
            for c in root:    
                root[1].text = a[:-4]+"_Flip.jpg"
        
            tree.write(os.getcwd +"/output/bbox_flip" + a[:-4]+"_Flip.xml", xml_declaration=True, method="xml", encoding="utf8")    

    

    

    
