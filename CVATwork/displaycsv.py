import matplotlib.pyplot as plt
import cv2
import pandas as pd

def displaycsv(path1,path2):
    ant=pd.read_csv(path1)
    for i in range(len(ant)):
        j=int(ant["frameno"][i])
        img=cv2.imread(path2+"/"+"0"*(3-len(str(j)))+str(j)+".jpg")

        img = cv2.rectangle(img, (int(ant['left'][i]),int(ant['top'][i])), (int(ant['right'][i]),int(ant['bottom'][i])),(0,0,255),3)             #print(i)       
        cv2.imwrite("annotated_frames/annotated_frames"+str(ant.iloc[i,0])+".jpg",img)
    
    