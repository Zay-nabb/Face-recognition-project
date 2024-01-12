import os
import pickle
import numpy as np
import cv2
import face_recognition

# parameters identifiers:
#  0 is for webcam
# 1 is for External Camera "any Other Camera"
cap = cv2.VideoCapture(0)

# as background of squre which will show our faces in GUI Its Dimensions 640px for height and 480px for width
# to acess width dimensions use 3 and we typed it's value as 640px
# to acess height dimensions use 4 and we typed it's value as 480px
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread('Resources/background.jpg')

# importing the modes that will describe faces state whether it's registered or not in our database
# we stored the modes images in a data collection (List).

# identify The Full Path For The Whole folder to easy access the data.
folderModePath='Resources/Modes'
# list directory extract ( Files Path ) from the selected Folder (Folder Mode Path "The Variable Upside").
modePathList = os.listdir(folderModePath)  # Returns A List.
imgModeList = []

# for each image we will read the image by it's path by used os library to access the full path.
for path in modePathList:
    # we used os.join as a concatination method just for access the full path for the image (Concatenate The General Folder (Folder Mode Path))
    # with the selected image in the list according to it's order in the loop
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))   # here we get a list for the full path of the image now.

#print(len(imgModeList))

# loading the encodings file in a form of binary system information as the library mainly depends on binary form in arrays.
file = open('EncodeFile.p', 'rb')  # file mode reading in binary format.


# file is a file of two lists : ( array ) one for the 128 encodings " Face Details " , and the other list is for Ids
encodeListKnownWithIds = pickle.load((file))
file.close()

# we assign the list and array combined with encodeListKnownWithIds Varaiable in Two another Variables To Perform Our
# computational performance.
encodeListKnown, studentIds = encodeListKnownWithIds
print(studentIds)

while True:
    # read Function Return A Boolean Value (True if the frame is read correctly) in sucess and save the value (captured image pixels)
    # in image variable
    success, img = cap.read()
    # minimize the image to reduce the computional power and to save data and time ("Reducing Complexity")
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)


    # find faces location and generate their encodings in order to compare them with stored image encodings in our directory
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    imgBackground[162:162+480, 55:55+640] = img
    # imgBackground[44:44+633,808:808+414]=imgModeList[2]

    # loop through two lists with same time we have to use zip method to not give an error
    # in order to reduce complexity(memory and time) and not to use two separate loops separately

    for encoFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches=face_recognition.compare_faces(encodeListKnown, encoFace)  # Returns A List Of True And False
        faceDis=face_recognition.face_distance(encodeListKnown, encoFace)  # Returns A List Of Numbers Resemmbles The distance comparison

        # print("Matches",matches)
        # print("Face Distance",faceDis
        # to get the index of the least number from the faceDis List (Distance Comparison)
        matchIndex = np.argmin(faceDis)
        # print("Match Index",matchIndex)
        if matches[matchIndex]:
            print("Known Face Detected")
            imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[2]

            print(studentIds[matchIndex])
        else:
            print("Unknown Face")
            imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[0]

    # cv2.imshow("Webcam" , img)
    cv2.imshow("Face Recogniation ", imgBackground)
    cv2.waitKey(1)