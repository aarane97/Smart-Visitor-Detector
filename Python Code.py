import cv2
import face_recognition
import glob
import numpy as np
import serial

ser = serial.Serial('/dev/ttyACM1',9600,timeout=100)
while True:
    read_serial=ser.readline().strip()
    #s[0] = str(int (ser.readline(),16))
    #print (s[0])
    print ((read_serial))
    if read_serial:
        if (int(read_serial))<20:
            break


cam=cv2.VideoCapture(0)
_,img=cam.read()

cv2.namedWindow("camera", cv2.WINDOW_AUTOSIZE)
cv2.imwrite('/var/www/html/karanc/Clicked/2.png',img)
cv2.imshow("camera",img)
cv2.waitKey(0)
cv2.destroyWindow("camera")


images = [cv2.imread(file) for file in glob.glob("/var/www/html/karanc/known/*.png")]
n=len(images)
#print(n)

k_encoding=np.zeros((n,128))

for i in range(n):
    #k_image[i] = face_recognition.load_image_file(images[i])
    k_encoding[i]= face_recognition.face_encodings(images[i])[0]
   
unknown_image = face_recognition.load_image_file("/var/www/html/karanc/Clicked/2.png")
unknown_encoding = face_recognition.face_encodings(unknown_image)

known_faces = []
for j in range(n):
    known_faces.append(k_encoding[j])

if len(unknown_encoding) > 0:
        unknown_face_encoding = unknown_encoding[0]

        results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

        m=0
        for i in range(n):
            if results[i] == True:
                m=1
                break
        print(m)

        if m==0:
            cv2.imwrite('/var/www/html/karanc/images/2.png',img)
    
