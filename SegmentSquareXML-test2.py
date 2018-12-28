# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 10:36:09 2018

@author: IMRANKHAN
"""

import os
import xml.etree.ElementTree as ET



def getArea(x1,x2,y1,y2):
    area = (y1*x2 + y1*x2 + y2*x1 + y2*x1) - (x1*y1 + x2*y2 + x2*y2 + x1*y1)
    return abs(area)//2


def bboxCrop(xml_dir,threshold,i):
    
    for a in os.listdir(xml_dir):
    
        with open(xml_dir+a, encoding="utf8") as f:    
        
            tree = ET.parse(xml_dir+a)
            root = tree.getroot()

            for c in root:
                w1 = root[1].text 
                w2 = w1[:-4]
                width = int(root[4][0].text)
                height = int(root[4][1].text)
                
            for b in root.findall(".//object"):   
                xmin = int(b[4][0].text)
                xmax = int(b[4][2].text)            
                ymin = int(b[4][1].text)
                ymax = int(b[4][3].text)
            
                OGarea = getArea(xmin, xmax, ymin, ymax)
                
                if OGarea==0:
                    root.remove(b)
                
                if i==1:
                    x2 = width//2
                    y2 = height//2
                    
                    if xmax > x2:
                        b[4][2].text = str(x2)
                        xmax = int(b[4][2].text)
                        
                    if ymax > y2:
                        b[4][3].text = str(y2)
                        ymax = int(b[4][3].text)
                    
                    Croparea = getArea(xmin, xmax, ymin, ymax)
                    
                    if Croparea/OGarea < threshold or xmin>x2 or ymin>ymax:
                        root.remove(b)
                        print(w2 +": "+ b[0].text + " REMOVED!")


                if i==2:
                    x2 = width//2
                    y1 = height//2
                    
                    if xmax > x2:
                        b[4][2].text = str(x2)
                        xmax = int(b[4][2].text)
                        
                    if ymin < y1:
                        b[4][1].text = str(y1)
                        ymin = int(b[4][1].text)
                        
                    ymin2 = ymin - y1
                    ymax2 = ymax - y1
                    
                    b[4][1].text = str(ymin2)
                    b[4][3].text = str(ymax2)
                    
                    Croparea = getArea(xmin, xmax, ymin2, ymax2)
                    
                    if Croparea/OGarea < threshold or ymin2>ymax2 or xmin>xmax:
                        root.remove(b)
                        print(w2 +": "+ b[0].text+" REMOVED!")
                    
                if i==3:
                    x1 = width//2
                    y2 = height//2
                    
                    if xmin < x1 :
                        b[4][0].text = str(x1)
                        xmin = int(b[4][0].text)
                        
                    if ymax > y2:
                        b[4][3].text = str(y2)
                        ymax = int(b[4][3].text)
                        
                    xmin2 = xmin - x1
                    xmax2 = xmax - x1
                    
                    b[4][0].text = str(xmin2)
                    b[4][2].text = str(xmax2)
                    
                    Croparea = getArea(xmin2, xmax2, ymin, ymax)
                    
                    if Croparea/OGarea < threshold or xmax2<0 or xmin2<0 or xmin2>xmax2 or ymin>ymax:
                        root.remove(b)
                        print(w2 +": "+ b[0].text+" REMOVED!")
                    
                if i==4:
                    x1 = width//2
                    y1 = height//2
                    
                    if xmin < x1 :
                        b[4][0].text = str(x1)
                        xmin = int(b[4][0].text)
                        
                    if ymin < y1:
                        b[4][1].text = str(y1)
                        ymin = int(b[4][1].text)
                        
                    xmin2 = xmin - x1
                    xmax2 = xmax - x1
                    ymin2 = ymin - y1
                    ymax2 = ymax - y1
                    
                    b[4][0].text = str(xmin2)
                    b[4][2].text = str(xmax2)
                    b[4][1].text = str(ymin2)
                    b[4][3].text = str(ymax2)
                    
                    Croparea = getArea(xmin2, xmax2, ymin2, ymax2)
                    
                    if Croparea/OGarea < threshold or xmax2<0 or xmin2<0 or xmin2>xmax2 or ymin2>ymax2:
                        root.remove(b)
                        print(w2 +": "+ b[0].text+" REMOVED!")
                    
                if i==5:
                    x1 = width//4
                    x2 = (3*width)//4
                    y1 = height//4
                    y2 = (3*height)//4
                    
                    if xmin < x1 :
                        b[4][0].text = str(x1)
                        xmin = int(b[4][0].text)
                        
                    if ymin < y1 :
                        b[4][1].text = str(y1)
                        ymin = int(b[4][1].text)
                        
                    if xmax > x2 :
                        b[4][2].text = str(x2)
                        xmax = int(b[4][2].text)
                        
                    if ymax > y2:
                        b[4][3].text = str(y2)
                        ymax = int(b[4][3].text)
                        
                    xmin2 = xmin - x1
                    xmax2 = xmax - x1
                    ymin2 = ymin - y1
                    ymax2 = ymax - y1
                    
                    b[4][0].text = str(xmin2)
                    b[4][2].text = str(xmax2)
                    b[4][1].text = str(ymin2)
                    b[4][3].text = str(ymax2)
                    
                    Croparea = getArea(xmin2, xmax2, ymin2, ymax2)
                    
                    if Croparea/OGarea < threshold or xmin2<0 or xmax2<0 or ymin2<0 or ymax2<0 or ymin2>ymax2 or xmin2>xmax2:
                        root.remove(b)
                        print(w2 +": "+ b[0].text+" REMOVED!")
                    
                if i==6:
                    x1 = width//4
                    x2 = (3*width)//4
                    y2 = height//2
                    
                    if xmin < x1:
                        b[4][0].text = str(x1)
                        xmin = int(b[4][0].text)
                        
                    if xmax > x2:
                        b[4][2].text = str(x2)
                        xmax = int(b[4][2].text)
                        
                    if ymax > y2:
                        b[4][3].text = str(y2)
                        ymax = int(b[4][3].text)
                        
                    xmin2 = xmin - x1
                    xmax2 = xmax - x1
                    
                    b[4][0].text = str(xmin2)
                    b[4][2].text = str(xmax2)
                    
                    Croparea = getArea(xmin2, xmax2, ymin, ymax)
                    
                    if Croparea/OGarea < threshold or xmax2<0 or xmin2<0 or xmin2>xmax2 or ymin>ymax:
                        root.remove(b)
                        print(w2 +": "+ b[0].text+" REMOVED!")

                if i==7:
                    x2 = width//2
                    y1 = height//4
                    y2 = (3*height)//4
                    
                    if xmax > x2 :
                        b[4][2].text = str(x2)
                        xmax = int(b[4][2].text)
                        
                    if ymin < y1:
                        b[4][1].text = str(y1)
                        ymin = int(b[4][1].text)
                        
                    if ymax > y2:
                        b[4][3].text = str(y2)
                        ymax = int(b[4][3].text)
                        
                    ymin2 = ymin - y1
                    ymax2 = ymax - y1
                    
                    b[4][1].text = str(ymin2)
                    b[4][3].text = str(ymax2)
                    
                    Croparea = getArea(xmin, xmax, ymin2, ymax2)
                    
                    if Croparea/OGarea < threshold or ymax2<0 or ymin2<0 or ymin2>ymax2 or xmin>xmax:
                        root.remove(b)
                        print(w2 +": "+ b[0].text+" REMOVED!")
                    
                if i==8:
                    x1 = width//4
                    x2 = (3*width)//4
                    y1 = height//2
                    
                    if xmin < x1 :
                        b[4][0].text = str(x1)
                        xmin = int(b[4][0].text)
                        
                    if xmax > x2:
                        b[4][2].text = str(x2)
                        xmax = int(b[4][2].text)
                        
                    if ymin < y1:
                        b[4][1].text = str(y1)
                        ymin = int(b[4][1].text)
                        
                    xmin2 = xmin - x1
                    xmax2 = xmax - x1
                    ymin2 = ymin - y1
                    ymax2 = ymax - y1
                    
                    b[4][0].text = str(xmin2)
                    b[4][2].text = str(xmax2)
                    b[4][1].text = str(ymin2)
                    b[4][3].text = str(ymax2)
                    
                    Croparea = getArea(xmin2, xmax2, ymin2, ymax2)
                    
                    if Croparea/OGarea < threshold or xmax2<0 or xmin2<0 or xmin2>xmax2 or ymin2>ymax2:
                        root.remove(b)
                        print(w2 +": "+ b[0].text+" REMOVED!")
                        
                if i==9:
                    x1 = width//2
                    y1 = height//4
                    y2 = (3*height)//4
                    
                    if xmin < x1 :
                        b[4][0].text = str(x1)
                        xmin = int(b[4][0].text)
                        
                    if ymin < y1:
                        b[4][1].text = str(y1)
                        ymin = int(b[4][1].text)
                    
                    if ymax > y2:
                        b[4][3].text = str(y2)
                        ymax = int(b[4][3].text)
                        
                    xmin2 = xmin - x1
                    xmax2 = xmax - x1
                    ymin2 = ymin - y1
                    ymax2 = ymax - y1
                    
                    b[4][0].text = str(xmin2)
                    b[4][2].text = str(xmax2)
                    b[4][1].text = str(ymin2)
                    b[4][3].text = str(ymax2)
                    
                    Croparea = getArea(xmin2, xmax2, ymin2, ymax2)
                    
                    if Croparea/OGarea < threshold or ymax2<0 or xmin2<0 or ymin2<0 or ymin2>ymax2 or xmin2>xmax2:
                        root.remove(b)
                        print(w2 +": "+ b[0].text+" REMOVED!")
                    

            for k in root:
                root[1].text = w2 + "_Crop_"+ str(i) +".jpg"
                root[4][0].text = str(width//2)
                root[4][1].text = str(height//2)
                
        tree.write(w2 + "_Crop_"+ str(i) +".xml", xml_declaration=True, method="xml", encoding="utf8")
    
    
    

xml_dir = "C:/Users/imrankhan/MAXIS/sample_xml/"

t = 0.75

bboxCrop(xml_dir,t,1) 
bboxCrop(xml_dir,t,2)
bboxCrop(xml_dir,t,3)
bboxCrop(xml_dir,t,4)
bboxCrop(xml_dir,t,5) 
bboxCrop(xml_dir,t,6)
bboxCrop(xml_dir,t,7)
bboxCrop(xml_dir,t,8)
bboxCrop(xml_dir,t,9)