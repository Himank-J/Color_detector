#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import pandas as pd
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
image_path = args['image']
image = cv2.imread(image_path)

clicked = False
r = g = b = xcor = ycor = 0

index=["color","color_name","hex","R","G","B"]
cd = pd.read_csv('colors.csv', names=index, header=None)

def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(cd)):
        d = abs(R- int(cd.loc[i,"R"])) + abs(G- int(cd.loc[i,"G"]))+ abs(B- int(cd.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = cd.loc[i,"color_name"]
    return cname

def draw_function(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xcor,ycor, clicked
        clicked = True
        xcor = x
        ycor = y
        b,g,r = image[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
       
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)

while(1):

    cv2.imshow("image",image)
    if (clicked):
   
         cv2.rectangle(image,(20,20), (750,60), (b,g,r), -1)

        
        text = getColorName(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        
        
        cv2.putText(image, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)

        
        if(r+g+b>=600):
            cv2.putText(image, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False

       
    if cv2.waitKey(20) & 0xFF ==27:
        break
    
cv2.destroyAllWindows()





get_ipython().run_line_magic('tb', '')


# In[ ]:




