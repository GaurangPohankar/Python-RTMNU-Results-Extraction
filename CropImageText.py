import re
import os
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import csv
import cv2

#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

fields = ['name', 'mom_name', 'department','cgpa','marks','result']
out_file = open('data.csv','w')
csvwriter = csv.DictWriter(out_file, delimiter=',', fieldnames=fields)
dict_service = {}

#text=re.sub(r'\s+', '', text)

img = cv2.imread('896193.png')

cv2.imshow("cropped", img)

crop_img = img[50:60, 127:400] #Crop from {x, y, w, h } => {0, 0, 300, 400}
#cv2.imshow("cropped", crop_img)
name = pytesseract.image_to_string(crop_img)
print(name)
dict_service['name'] = name

crop_img = img[60:80, 120:400] #Crop from {x, y, w, h } => {0, 0, 300, 400}
#cv2.imshow("cropped", crop_img)
mom_name = pytesseract.image_to_string(crop_img)
print(mom_name)
dict_service['mom_name'] = mom_name


crop_img = img[370:400, 250:440] #Crop from {x, y, w, h } => {0, 0, 300, 400}
#cv2.imshow("cropped", crop_img)
cgpa = pytesseract.image_to_string(crop_img)
print(cgpa)
dict_service['cgpa'] = cgpa


crop_img = img[370:400, 430:600] #Crop from {x, y, w, h } => {0, 0, 300, 400}
#cv2.imshow("cropped", crop_img)
marks = pytesseract.image_to_string(crop_img)
print(marks)
dict_service['marks'] = marks


crop_img = img[370:400, 600:750] #Crop from {x, y, w, h } => {0, 0, 300, 400}
#cv2.imshow("cropped", crop_img)
result = pytesseract.image_to_string(crop_img)
print(result)
dict_service['result'] = result


crop_img = img[80:100, 120:400] #Crop from {x, y, w, h } => {0, 0, 300, 400}
#cv2.imshow("cropped", crop_img)
department = pytesseract.image_to_string(crop_img)
print(department)
dict_service['department'] = department

with open('data.csv', 'a') as csvfile:
    filewriter = csv.DictWriter(csvfile, delimiter=',', fieldnames=fields)
    filewriter.writerow(dict_service)
    csvfile.close()
    #Write row to CSV
    csvwriter.writerow(dict_service)
