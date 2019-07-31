import re
import os
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import csv
import cv2


fields = ['name', 'mom_name', 'department','cgpa','marks','result']
out_file = open('data.csv','w')
csvwriter = csv.DictWriter(out_file, delimiter=',', fieldnames=fields)
dict_service = {}


img = cv2.imread('896193.png')
#cv2.imshow("cropped", img)

crop_img = img[190:205, 150:400] #Crop from {x, y, w, h } => {0, 0, 300, 400}
cv2.imshow("cropped", crop_img)
name = pytesseract.image_to_string(crop_img)
print(name)
dict_service['name'] = name


crop_img = img[197:220, 150:400] #Crop from {x, y, w, h } => {0, 0, 300, 400}
cv2.imshow("cropped", crop_img)
mom_name = pytesseract.image_to_string(crop_img)
print(mom_name)
dict_service['mom_name'] = mom_name


crop_img = img[225:245, 140:400] #Crop from {x, y, w, h } => {0, 0, 300, 400}
cv2.imshow("cropped", crop_img)
department = pytesseract.image_to_string(crop_img)
print(department)
dict_service['department'] = department



