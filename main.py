import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
import mysql.connector
import math
from tabulate import tabulate
import os
from dotenv import load_dotenv

load_dotenv()

def menuDrivenSelection():
    MaxInputNumber = 5
    FileName = ''
    print("MENU")
    print("Type 1 for Image 1")
    print("Type 2 for Image 2")
    print("Type 3 for Image 3")
    print("Type 4 for Image 4")
    print("Type 5 for Image 5")
    global choice
    choice = input("Which image would you like to select ? ")
    while not (choice.isdigit() and 0 < int(choice) <= MaxInputNumber) :
        print("Invalid Option. Please try again")
        choice = input("Which image would you like to select ? ")

    print("User selected Image" , choice)
    choice = int(choice)

    if choice == 1:
        FileName = "1.jpg"
    elif choice == 2:
        FileName = "2.jpg"
    elif choice == 3:
        FileName = "3.jpeg"
    elif choice == 4:
        FileName = "4.jpg"
    elif choice == 5:
        FileName = "5.jpg"
    else: 
        print("This file does not exist.")
    
    
    plt.imshow(cv2.cvtColor(cv2.imread(FileName), cv2.COLOR_BGR2RGB))
    plt.show()

    while True:
        conf = input("\nAre you sure you want to select this image(Y/N)? ")
        if conf in ["y", "Y"]:
            break
        elif conf in ["n","N"]:
            menuDrivenSelection()
        else:
            print("Invalid Option. Please try again") 
    calculateImage(FileName)

def difference(maxY,minY):
    diff = maxY - minY
    return diff

def calculateImage(FileName): 
    global vehicle 
    vehicle = 0
    im = cv2.imread(FileName)
    maxY = im.shape[0]
    # print(maxY)
    bbox, label, conf = cv.detect_common_objects(im)
    minY = bbox[0][1]
    maximumAllowedPixels = 150
    for i in range(len(bbox)):
        box = bbox[i]
        if box[1] < maximumAllowedPixels:
            pass
        else:
            minY = min(minY, box[1])
            if label[i] in ["car" , "bus" , "truck"]:
                vehicle += 1
    output_image = draw_bbox(im, bbox, label, conf)
    plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
    plt.show()
    # print('Number of vehciles in the image is', vehicle)

    diff = difference(maxY,minY)
    # print("difference is ", x)

    def find():
        diff = difference(maxY,minY)
        time = diff/20
        global times
        times = math.ceil(time)
        if 10 < vehicle <= 20:
            times = times
        elif 20 < vehicle <= 30:
            times += times*0.5
        elif 30 < vehicle <= 40:
            times += times*1
        elif vehicle > 40:
            times += times*1.5
            
        if times > 60:
            times = 60
            print("\nThe most suitable time for the green light would be" , times , "seconds.")
            print("Max time is capped at the 60 second limit.")
        else:
            print("The most suitable time for the green light would be" , times , "seconds.")
    find()
    def mysql_connector():
        mydb = mysql.connector.connect(
                host=os.getenv('DB_HOST'),
                user=os.getenv('DB_USER'),
                passwd=os.getenv('DB_PASSWORD'),
                database=os.getenv('DB_NAME')
            )        
        mycursor = mydb.cursor()
        d ='image'+ str(choice)
        z=str(d)
        x = vehicle
        q = maxY
        a = minY
        w = diff
        y = times
        try: 
            query="""INSERT INTO traffic VALUES (%s,%s,%s,%s,%s,%s)"""
            tup1=(z, x, q, a, w, y)
            mycursor.execute(query,tup1)
            query2='Select * from traffic where Image_No=(%s)'
            tup2=(z,)
            mycursor.execute(query2,tup2)
            myrecords = mycursor.fetchall()
            l=[['Image_No','No_of_Vehciles','MaxY','MinY','Difference','Time(sec)']]
            for x in myrecords:
                y=list(x)
                l.append(y)
            print(tabulate(l))
            mydb.commit()
            print("Record added to MySQL table 'traffic'.")
        except mysql.connector.IntegrityError:
            query2='Select * from traffic where Image_No=(%s)'
            tup2=(z,)
            mycursor.execute(query2,tup2)
            myrecords = mycursor.fetchall()
            l=[['Image_No','No_of_Vehciles','MaxY','MinY','Difference','Time(sec)']]
            for x in myrecords:
                y=list(x)
                l.append(y)
            print(tabulate(l))
            print("Above record already present in MySQL table 'traffic'.")


    mysql_connector()

menuDrivenSelection()
