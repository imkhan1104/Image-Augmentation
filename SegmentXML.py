tpu# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 15:23:20 2018

@author: IMRANKHAN
"""
import os
import xml.etree.ElementTree as ET



def getArea(x1,x2,y1,y2):
    area = (y1*x2 + y1*x2 + y2*x1 + y2*x1) - (x1*y1 + x2*y2 + x2*y2 + x1*y1)
    return abs(area)//2


def bboxCrop(x1,x2,xml_dir,threshold,i):
    
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
                    
                    Croparea = getArea(xmin, xmax, ymin, ymax)
                    
                    if Croparea/OGarea < threshold or xmin>x2:
                        root.remove(b)
                        print(w +": "+ b[0].text + " REMOVED!")


                if i==2:
                    if xmin < x1 :
                        b[4][0].text = str(x1)
                        xmin = int(b[4][0].text)
                
                    if xmax > x2:
                        b[4][2].text = str(x2)
                        xmax = int(b[4][2])
                        
                    xmin2 = xmin - 2736
                    xmax2 = xmax - 2736
                    b[4][0].text = str(xmin2)
                    b[4][2].text = str(xmax2)
                    
                    Croparea = getArea(xmin2, xmax2, ymin, ymax)
                    
                    if Croparea/OGarea < threshold or xmax2<0 or xmin2<0:
                        root.remove(b)
                        print(w +": "+ b[0].text+" REMOVED!")
                

                if i==3:
                    if xmin < x1 :
                        b[4][0].text = str(x1)
                        xmin = int(b[4][0].text)
                        
                    if xmax > x2:
                        b[4][2].text = str(x2)
                        xmax = int(b[4][2].text)
                        
                    xmin2 = xmin - 1368
                    xmax2 = xmax - 1368
                    b[4][0].text = str(xmin2)
                    b[4][2].text = str(xmax2)
                    
                    Croparea = getArea(xmin2, xmax2, ymin, ymax)
                    
                    if Croparea/OGarea < threshold or xmax2<0 or xmin2<0 or xmin2>xmax2:
                        root.remove(b)
                        print(w +": "+ b[0].text+" REMOVED!")

                
        tree.write(w + "_Crop_"+ str(i) +".xml", xml_declaration=True, method="xml", encoding="utf8")
    
    
    


xml_dir = "C:/Users/imrankhan/MAXIS/sample_xml/"

t = 0.5


bboxCrop(0,2736,xml_dir,t,1) 

bboxCrop(2736,5472,xml_dir,t,2)

bboxCrop(1368,4104,xml_dir,t,3) 



            
            
            
            