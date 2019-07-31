import urllib.request
import time
from selenium import webdriver
from getpass import getpass
from selenium.webdriver.support.ui import Select
import re
import os
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import csv
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

fields = ['name', 'mom_name', 'department','result','subject1','subjectmark1','subject2',
          'subjectmark2','subject3','subjectmark3','subject4','subjectmark4','subject5',
          'subjectmark5','subject6','subjectmark6','subject7','subjectmark7','total_marks','sgpa']
out_file = open('data.csv','w')
csvwriter = csv.DictWriter(out_file, delimiter=',', fieldnames=fields)
dict_service = {}

'''
header = ['Student Name', 'Mother Name', 'Department', 'Compilers',
         'Compilers Lab', 'Artificial Intelligence', 'Artificial Intelligence Lab',
         'Ele-I', 'Ele-II', 'Project']
'''
#make sure that geckodriver in place with this file
#Google Chrome/firefox should be installed

driver = webdriver.Chrome(executable_path="C:/Users/windows/Desktop/python/chromedriver")
#driver = webdriver.Firefox(executable_path='./geckodriver')
driver.maximize_window()

def readimg(value):
    try:
        img = cv2.imread(value)
        cv2.imshow("cropped", img)

        crop_img = img[180:205, 150:400] #Crop from {x, y, w, h } => {0, 0, 300, 400}
        cv2.imshow("NAME", crop_img)
        name = pytesseract.image_to_string(crop_img)
        print(name)
        dict_service['name'] = name

        crop_img = img[197:210, 150:400] #Crop from {x, y, w, h } => {0, 0, 300, 400}
        cv2.imshow("MOTHER", crop_img)
        mom_name = pytesseract.image_to_string(crop_img)
        print(mom_name)
        dict_service['mom_name'] = mom_name

        crop_img = img[220:240, 140:400] #Crop from {x, y, w, h } => {0, 0, 300, 400}
        cv2.imshow("DEPARTMENT", crop_img)
        department = pytesseract.image_to_string(crop_img)
        print(department)
        dict_service['department'] = department

        crop_img = img[300:400, 60:350] #Crop from {x, y, w, h } => {0, 0, 300, 400}
        cv2.imshow("SUBJECT", crop_img)
        subject = pytesseract.image_to_string(crop_img)


        subject = subject.splitlines(True)
        subject = [x.replace('\n', '') for x in subject]
        for item in subject:
            if len(item) < 1:  
                subject.remove(item)
        print(subject)
        
        dict_service['subject1'] = subject[0]
        dict_service['subject2'] = subject[1]
        dict_service['subject3'] = subject[2]
        dict_service['subject4'] = subject[3]
        dict_service['subject5'] = subject[4]
        dict_service['subject6'] = subject[5]
        dict_service['subject7'] = subject[6]
        
        crop_img = img[300:400, 350:700] #Crop from {x, y, w, h } => {0, 0, 300, 400}
        cv2.imshow("MARKS", crop_img)
        marks = pytesseract.image_to_string(crop_img)
        marks =  re.split('\s+', marks)
        #print(marks)
        #print(marks[:7])
        college_marks = marks[:7]
        total_marks = marks[7:]
        total_marks = total_marks[:7]
        minimum_marks = marks[14:]
        minimum_marks = minimum_marks[:7]
        obtained_marks = marks[21:]
        obtained_marks = obtained_marks[:6]
        practical_marks = marks[27:]
        practical_marks = practical_marks[:7]
        student_marks = marks[-7:]

        print(college_marks)
        print(total_marks)
        print(minimum_marks)
        print(obtained_marks)
        print(practical_marks)
        print(student_marks)
        #print(marks[-7:])

        dict_service['subjectmark1'] = student_marks[0]+"/"+total_marks[0]
        dict_service['subjectmark2'] = student_marks[1]+"/"+total_marks[1]
        dict_service['subjectmark3'] = student_marks[2]+"/"+total_marks[2]
        dict_service['subjectmark4'] = student_marks[3]+"/"+total_marks[3]
        dict_service['subjectmark5'] = student_marks[4]+"/"+total_marks[4]
        dict_service['subjectmark6'] = student_marks[5]+"/"+total_marks[5]
        dict_service['subjectmark7'] = student_marks[6]+"/"+total_marks[6]
        
        
        crop_img = img[450:550, 200:680] #Crop from {x, y, w, h } => {0, 0, 300, 400}
        cv2.imshow("RESULT", crop_img)
        result = pytesseract.image_to_string(crop_img)
        non_decimal = re.compile(r'[^\d.]+')
        result = non_decimal.sub(' ', str(result))
        result = re.split('\s+', result)
        result = [x for x in result if len(str(x)) > 2]
        dict_service['sgpa'] = result[0]+"/10"
        print(result)

        
        with open('data.csv', 'a') as csvfile:
            filewriter = csv.DictWriter(csvfile, delimiter=',', fieldnames=fields)
            filewriter.writerow(dict_service)
        csvfile.close()
        # Write row to CSV
        csvwriter.writerow(dict_service)
        #os.remove(value)
    except:
        print('No Info Found')

for num in range(896193,896212):
    try:
        # Open rtmnu Page
        driver.get("https://rtmnuresults.org/")
        time.sleep(2)

        select = Select(driver.find_element_by_id('ddlselectfaculty'))
        time.sleep(2)
        # select by visible text
        select.select_by_visible_text('Faculty of Science & Technology')
        time.sleep(5)

        select = Select(driver.find_element_by_id('ddlselectexam'))
        time.sleep(5)

        #select.select_by_visible_text('B.E. Sixth Semester [CBS] (Reassessment)')
        select.select_by_value('2026')
        time.sleep(5)

        element = driver.find_element_by_id("txtrollno")
        element.send_keys(num)

        next = driver.find_element_by_id("imgbtnviewmarksheet").click()
                                 
        # select by value 
        #select.select_by_value('103')
        time.sleep(5)

        driver.save_screenshot(str(num)+".png")
        readimg(str(num)+".png")
        #driver.close()
    except:
        print('Something Went wrong')
