# Face-recognition-project
A live face recognition project that detects faces using webcam and determine whether this face is registered in it's system or not, it is so helpful in attendance system by recognizing faces.
Used language : Python.
Used libraries : dlib, face-recognition.
# detailed explaination (two stages)
First, the code stage:
  A punch of images are added ton the project file and the code takes the distances and encodings of this face details and save the 128 encoding plus details in a file 
Second, On run stage:
  the webcam opens and take captures these captures are sent to take their encodings and compare them with what already in the system inside the system, if the encodings are matched it         display an image "marked" and prints the face ID, otherwise display "active".      

![Screenshot 2024-01-12 232704](https://github.com/Zay-nabb/Face-recognition-project/assets/156392721/6c5adad4-9975-4f92-a754-2014bb43fa53)

  # Libraries used

  ![Screenshot 2024-01-12 234417](https://github.com/Zay-nabb/Face-recognition-project/assets/156392721/5ee5f9d5-3c08-48f6-9086-77721d46ee46)
  
  
# Files 
files are classified to (images, modes, data file, encode-generator function, main file that has the program.
images: upload the images you want to save their encodings in the permenant file in order to compare what will be captured by the webcam with them.
modes : tells if the recognized face is not in the system by active or found by marked.
data file : that saves all the system images' encodings in it.
encode-generator : the file that has the code of that generates the encodings of the images in the system.
main file : where we run the program and opens the webcam and calls the encode-generator function.     


![Screenshot 2024-01-12 233753](https://github.com/Zay-nabb/Face-recognition-project/assets/156392721/5827e0e5-bafc-4e82-aac3-b9f88bb4a23e
)

# sample from Encode Generator 

![Screenshot 2024-01-12 235156](https://github.com/Zay-nabb/Face-recognition-project/assets/156392721/b9f1a97c-87e5-458b-8c92-260fe0a87eee)

# sample from the while loop that functions while the webcam is open

![Screenshot 2024-01-12 235806](https://github.com/Zay-nabb/Face-recognition-project/assets/156392721/c0a826e0-0310-47ae-9449-a96bfc883548)
