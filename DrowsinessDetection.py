import cv2 
import numpy as np 
import dlib 
from gtts import gTTS
from playsound import playsound
import os
import pyttsx3



wavFile = "beep.mp3"

# other method
#from win32com.client import Dispatch
#speak = Dispatch("SAPI.SpVoice")

area = 0

def alarm():

    #os.system("afplay beep.wav&")
    
    # other method
    #speak.Speak("warning")
    #message = "Wake up"
    #language = 'hi'
    #output = gTTS(text = message, lang= language, slow = False)
    #output.save("hola.mp3")
    print("-----------------threshold------------------------")
    playsound("beep.mp3")
    #os.remove("hola.mp3")
    print("--------ending beep----------------------------------")
    



def find_area(array):
    a = 0
    ox,oy = array[0]
    for x,y in array[1:]:
        a += abs(x*oy-y*ox)
        ox,oy = x,y
    return a/2

def start():
    camera = cv2.VideoCapture(0) 
    # We initialise detector of dlib 
    detector = dlib.get_frontal_face_detector() 
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") 
    # Start the main program 
    while camera.isOpened(): 
        ret, frame = camera.read()
        print(ret)
        if ret:
            # We actually Convert to grayscale conversion 
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
            faces = detector(gray) 
            for face in faces: 
            # The face landmarks code begins from here 
                x1 = face.left() 
                y1 = face.top() 
                x2 = face.right() 
                y2 = face.bottom() 
                # Then we can also do cv2.rectangle function (frame, (x1, y1), (x2, y2), (0, 255, 0), 3) 
                landmarks = predictor(gray, face) 
                
                # We are then accesing the landmark points 
                Landarkss = [] 
                for n in range(48, 55): 
                    x = landmarks.part(n).x 
                    y = landmarks.part(n).y 
                    print("Landmark1--->",(x,y))
                    Landarkss.append((x,y))
                    cv2.circle(frame, (x, y), 2, (255, 255, 255), -1) 
                Landarkss2 = [] 
                for n in range(54, 61): 
                    x = landmarks.part(n).x 
                    y = landmarks.part(n).y 
                    print("Landmark2--->",(x,y))
                    Landarkss.append((x,y))
                    cv2.circle(frame, (x, y), 2, (255, 255, 255), -1) 
                #print("Landmarks--->",Landarkss)

                array = Landarkss + Landarkss2
                print("Landmarks--->",array)
                area = find_area(array)
                print("Total area--->", area)
               
                YAWN_THRESH = 26000
                if (area > YAWN_THRESH):
                    alarm()  
                    print("You yawned")  
                #else:
                #    pass
                
            cv2.imshow("Frame", frame) 

            key = cv2.waitKey(1) 
            if key%256 == 27: 
                break # press esc the frame is destroyed (edited) 

start()