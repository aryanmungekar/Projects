import face_recoginition
import cv2
import numpy as np
import csv
import os
from datetime import datetime

video_capture = cv2.VideoCapture(0)

gates_image = face_recognition.load_image_file(photos/gates.jpeg)
gates_encoding = face_recognition.face_encoding(gates_image)[0]

ambani_image = face_recognition.load_image_file(photos/ambani.jpeg)
ambani_encoding = face_recognition.face_encoding(ambani_image)[0]

elon_image = face_recognition.load_image_file(photos/elon.jpeg)
elon_encoding = face_recognition.face_encoding(elon_image)[0]

jeff_image = face_recognition.load_image_file(photos/jeff.jpeg)
jeff_encoding = face_recognition.face_encoding(jeff_image)[0]

known_face_encoding = [
gates_encoding,
ambani_encoding,
elon_encoding,
jeff_encoding,
]

known_faces_names = [
"gates",
"ambani",
"elon",
"jeff",
]

students = known_faces_names.copy()

face_locations = []
face_encodings = []
face_names = []
s=True


now = datetime.now()
current_date = now.strftime("%Y-%m-%d")



f = open(current_date+'.csv','w+',newline= '')
lnwriter = csv.writer(f)

while True:
    _,frame = video_capture.read()
    small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame = small_frame[:,:,::-1]
    if s:
        face_locations = face_recoginition.face_locations(rgb_small_frame)
        face_encodings = face_recoginition.face_encodings(rgb_small_frame,face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
            name=""
            face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
            best_match_index = np.argimn(face_distance)
            if matches[best_match_index]:
                name - known_faces_names[best_match_index]


