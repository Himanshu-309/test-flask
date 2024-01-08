import cv2
import os
 
def detectFace(image_content):
    print("\nRunning DetectFaceDemo")

    # Create a face detector from the cascade file
    face_cascade = cv2.CascadeClassifier("C:/Users/Himanshu/Downloads/python_API/python_API/app/modules/haarcascade_frontalface_default.xml")
    # face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
     
    print("dsf---- ", len(image_content))
    # Create an image file from the bytes
    image_path = "temp_image.png"
    with open(image_path, 'wb') as temp_file:
        temp_file.write(image_content)

    # Read the image
    image = cv2.imread(image_path)

    # Remove the temporary image file
    os.remove(image_path)
    
     # Check if the image is properly loaded
    # print("Image Size:", image.shape)

    if face_cascade.empty():
        print("Face cascade not loaded")
        return
    if image is None or image.size == 0:
        print("Failed to read image")
        return

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    face_detections = face_cascade.detectMultiScale(
        gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    print(f"Detected {len(face_detections)} faces") 
    
    # crop the face
    for (x, y, w, h) in face_detections:
        # Crop the face
        print("Cropping the image.....") 
        face_image = image[y-40:y+h+40, x-40:x+w+40]
           
        # Resize the face to 100x100 
        resized_face = cv2.resize(face_image, (100, 100))
        
        #convert it into bytes string 
        image_bytes = cv2.imencode(".png", resized_face)[1].tobytes()

        # Save the resized face
        # print("Storing the image into output folder.....")
        # os.makedirs("faceDetected", exist_ok=True)
        # # print(f"Writing faceDetected")
        # cv2.imwrite("faceDetected/1.png", resized_face)
    return image_bytes
