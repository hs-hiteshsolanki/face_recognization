import face_recognition as fr
import cv2
import numpy as np
import glob,os
from datetime import datetime,date
from webcame.web import webcam



today = date.today()

datetime1=datetime.now()
current_time = datetime1.strftime("%H_%M_%S")

path = "./train/"

known_names = []
known_name_encodings = []

images = os.listdir(path)
for _ in images:
    image = fr.load_image_file(path + _)
    image_path = path + _
    encoding = fr.face_encodings(image)[0]

    known_name_encodings.append(encoding)
    known_names.append(os.path.splitext(os.path.basename(image_path))[0].capitalize())

print(known_names)

os.chdir("test")
flag=None
for file in glob.glob("*.jpg"):
    print(file)

    #test_image = "./test/test.jpg"
    image = cv2.imread(file)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    face_locations = fr.face_locations(image)
    face_encodings = fr.face_encodings(image, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = fr.compare_faces(known_name_encodings, face_encoding)
        name = ""
        #check to name in image for name
        face_distances = fr.face_distance(known_name_encodings, face_encoding)
        best_match = np.argmin(face_distances)

        if matches[best_match]:
            name = known_names[best_match]

        im=cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
        if im.all():
            flag = False
        else:
            flag = True

        # border hight and with
        cv2.rectangle(image, (left, bottom - 15), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        #write a name for check image
        cv2.putText(image, name, (left + 6, bottom - 6), font, 0.3, (255, 255, 255), 1)

    #date time featch
    datetime1 = datetime.now()
    current_time = datetime1.strftime("%H_%M_%S")

    def Create_Dir():
        try:
            os.mkdir(str(today))
        except:
            print("Directory already exist :")


    cv2.imshow("Result", image)
    Create_Dir()
    if flag:

        final_path ="{}/{}.jpg".format(str(today),str(current_time))
        print(final_path)
        cv2.imwrite(final_path, image)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()
    else:
        print("there is no human")
        cv2.waitKey(5000)
        cv2.destroyAllWindows()
        pass
