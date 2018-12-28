# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 16:23:36 2018

@author: imrankhan
"""

import os
import xml.etree.ElementTree as ET



def getArea(x1,x2,y1,y2):
    area = (y1*x2 + y1*x2 + y2*x1 + y2*x1) - (x1*y1 + x2*y2 + x2*y2 + x1*y1)
    return abs(area)//2


def bboxCrop(x1,x2,y1,y2,xml_dir,threshold,i):
    
    for a in os.listdir(xml_dir):
    
        with open(xml_dir+a, encoding="utf8") as f:    
        
            tree = ET.parse(xml_dir+a)
            root = tree.getroot()

            for c in root:
                w = root[1].text 
                w = w[:-4]
                
        
        
            for b in root.findall(".//object"):   
                xmin = int(b[4][0].text)
                xmax = int(b[4][2].text)            
                ymin = int(b[4][1].text)
                ymax = int(b[4][3].text)
            
                OGarea = getArea(xmin, xmax, ymin, ymax)
                
                if i==1:
                    if xmax > x2:
                        b[4][2].text = str(x2)
                        xmax = int(b[4][2].text)
                        
                    if ymax > y2:
                        b[4][3].text = str(y2)
                        ymax = int(b[4][3].text)
                    
                    Croparea = getArea(xmin, xmax, ymin, ymax)
                    
                    if Croparea/OGarea < threshold or xmin>x2 or ymin>ymax:
                        root.remove(b)
                        print(w +": "+ b[0].text + " REMOVED!")


                if i==2:
                
                    if xmax > x2:
                        b[4][2].text = str(x2)
                        xmax = int(b[4][2].text)
                        
                    if ymin < y1:
                        b[4][1].text = str(y1)
                        ymin = int(b[4][1].text)
                        
                    ymin2 = ymin - 1539
                    ymax2 = ymax - 1539
                    
                    b[4][1].text = str(ymin2)
                    b[4][3].text = str(ymax2)
                    
                    Croparea = getArea(xmin, xmax, ymin2, ymax2)
                    
                    if Croparea/OGarea < threshold or ymin2>ymax2 or xmin>xmax:
                        root.remove(b)
                        print(w +": "+ b[0].text+" REMOVED!")
                

                if i==3:
                    if xmin < x1 :
                        b[4][0].text = str(x1)
                        xmin = int(b[4][0].text)
                        
                    if ymax > y2:
                        b[4][3].text = str(y2)
                        ymax = int(b[4][3].text)
                        
                    xmin2 = xmin - 2736
                    xmax2 = xmax - 2736
                    
                    b[4][0].text = str(xmin2)
                    b[4][2].text = str(xmax2)
                    
                    Croparea = getArea(xmin2, xmax2, ymin, ymax)
                    
                    if Croparea/OGarea < threshold or xmax2<0 or xmin2<0 or xmin2>xmax2 or ymin>ymax:
                        root.remove(b)
                        print(w +": "+ b[0].text+" REMOVED!")
                        
                if i==4:
                    if xmin < x1 :
                        b[4][0].text = str(x1)
                        xmin = int(b[4][0].text)
                        
                    if ymin < y1:
                        b[4][1].text = str(y1)
                        ymin = int(b[4][1].text)
                        
                    xmin2 = xmin - 2736
                    xmax2 = xmax - 2736
                    ymin2 = ymin - 1539
                    ymax2 = ymax - 1539
                    
                    b[4][0].text = str(xmin2)
                    b[4][2].text = str(xmax2)
                    b[4][1].text = str(ymin2)
                    b[4][3].text = str(ymax2)
                    
                    Croparea = getArea(xmin2, xmax2, ymin2, ymax2)
                    
                    if Croparea/OGarea < threshold or xmax2<0 or xmin2<0 or xmin2>xmax2 or ymin2>ymax2:
                        root.remove(b)
                        print(w +": "+ b[0].text+" REMOVED!")
                        
                if i==5:
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
                        
                    xmin2 = xmin - 1368
                    xmax2 = xmax - 1368
                    ymin2 = ymin - 769
                    ymax2 = ymax - 769
                    
                    b[4][0].text = str(xmin2)
                    b[4][2].text = str(xmax2)
                    b[4][1].text = str(ymin2)
                    b[4][3].text = str(ymax2)
                    
                    Croparea = getArea(xmin2, xmax2, ymin2, ymax2)
                    
                    if Croparea/OGarea < threshold or xmin2<0 or xmax2<0 or ymin2<0 or ymax2<0 or ymin2>ymax2 or xmin2>xmax2:
                        root.remove(b)
                        print(w +": "+ b[0].text+" REMOVED!")
                        
                if i==6:
                    if xmin < x1:
                        b[4][0].text = str(x1)
                        xmin = int(b[4][0].text)
                        
                    if xmax > x2:
                        b[4][2].text = str(x2)
                        xmax = int(b[4][2].text)
                        
                    if ymax > y2:
                        b[4][3].text = str(y2)
                        ymax = int(b[4][3].text)
                        
                    xmin2 = xmin - 1368
                    xmax2 = xmax - 1368
                    
                    
                    b[4][0].text = str(xmin2)
                    b[4][2].text = str(xmax2)
                    
                    Croparea = getArea(xmin2, xmax2, ymin, ymax)
                    
                    if Croparea/OGarea < threshold or xmax2<0 or xmin2<0 or xmin2>xmax2 or ymin>ymax:
                        root.remove(b)
                        print(w +": "+ b[0].text+" REMOVED!")

                if i==7:
                    if xmax > x2 :
                        b[4][2].text = str(x2)
                        xmax = int(b[4][2].text)
                        
                    if ymin < y1:
                        b[4][1].text = str(y1)
                        ymin = int(b[4][1].text)
                        
                    if ymax > y2:
                        b[4][3].text = str(y2)
                        ymax = int(b[4][3].text)
                        
                    ymin2 = ymin - 769
                    ymax2 = ymax - 769
                    
                    b[4][1].text = str(ymin2)
                    b[4][3].text = str(ymax2)
                    
                    Croparea = getArea(xmin, xmax, ymin2, ymax2)
                    
                    if Croparea/OGarea < threshold or ymax2<0 or ymin2<0 or ymin2>ymax2 or xmin>xmax:
                        root.remove(b)
                        print(w +": "+ b[0].text+" REMOVED!")

                if i==8:
                    if xmin < x1 :
                        b[4][0].text = str(x1)
                        xmin = int(b[4][0].text)
                        
                    if xmax > x2:
                        b[4][2].text = str(x2)
                        xmax = int(b[4][2].text)
                        
                    if ymin < y1:
                        b[4][1].text = str(y1)
                        ymin = int(b[4][1].text)
                        
                    xmin2 = xmin - 1368
                    xmax2 = xmax - 1368
                    ymin2 = ymin - 1539
                    ymax2 = ymax - 1539
                    
                    b[4][0].text = str(xmin2)
                    b[4][2].text = str(xmax2)
                    b[4][1].text = str(ymin2)
                    b[4][3].text = str(ymax2)
                    
                    Croparea = getArea(xmin2, xmax2, ymin2, ymax2)
                    
                    if Croparea/OGarea < threshold or xmax2<0 or xmin2<0 or xmin2>xmax2 or ymin2>ymax2:
                        root.remove(b)
                        print(w +": "+ b[0].text+" REMOVED!")
                        
                if i==9:
                    if xmin < x1 :
                        b[4][0].text = str(x1)
                        xmin = int(b[4][0].text)
                        
                    if ymin < y1:
                        b[4][1].text = str(y1)
                        ymin = int(b[4][1].text)
                    
                    if ymax > y2:
                        b[4][3].text = str(y2)
                        ymax = int(b[4][3].text)
                        
                    xmin2 = xmin - 2736
                    xmax2 = xmax - 2736
                    ymin2 = ymin - 769
                    ymax2 = ymax - 769
                    
                    b[4][0].text = str(xmin2)
                    b[4][2].text = str(xmax2)
                    b[4][1].text = str(ymin2)
                    b[4][3].text = str(ymax2)
                    
                    Croparea = getArea(xmin2, xmax2, ymin2, ymax2)
                    
                    if Croparea/OGarea < threshold or ymax2<0 or xmin2<0 or ymin2<0 or ymin2>ymax2 or xmin2>xmax2:
                        root.remove(b)
                        print(w +": "+ b[0].text+" REMOVED!")



        for k in root.findall(".//object"):
            k[4][0].text = str(int(k[4][0].text) + 1)
            k[4][1].text = str(int(k[4][1].text) + 1)
            k[4][2].text = str(int(k[4][2].text) - 1)
            k[4][3].text = str(int(k[4][3].text) - 1)
            
        tree.write(w + "_Crop_"+ str(i) +".xml", xml_declaration=True, method="xml", encoding="utf8")
    
    
    


xml_dir = "C:/Users/imrankhan/MAXIS/sample_xml/"

t = 0.75

bboxCrop(0,2736,0,1539,xml_dir,t,1) 

bboxCrop(0,2736,1539,3078,xml_dir,t,2)

bboxCrop(2736,5472,0,1539,xml_dir,t,3)

bboxCrop(2736,5472,1539,3078,xml_dir,t,4)

bboxCrop(1368,4106,769,2309,xml_dir,t,5) 

bboxCrop(1368,4106,0,1539,xml_dir,t,6)

bboxCrop(0,2736,769,2309,xml_dir,t,7)

bboxCrop(1368,4106,1539,3078,xml_dir,t,8)

bboxCrop(2736,5472,769,2309,xml_dir,t,9)