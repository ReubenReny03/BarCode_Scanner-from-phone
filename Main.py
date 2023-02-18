import cv2
import numpy as np
from pyzbar.pyzbar import decode
import time
import winsound
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
address = ("ip_webcam") #get address from ip webcam app
cap.open(address)
data_base = []
while True:
    success, img = cap.read()
    for barcode in decode(img):
        if barcode.data not in data_base: # so that the scanned object only prints once
            print(barcode.data)
            data_base.append(barcode.data)
            winsound.Beep(1000,1000)
            time.sleep(2)
        else:
            cap.open(address) # resetting the capture so that buffer images get trashed
                              # to improve time
    cv2.waitKey(1)
