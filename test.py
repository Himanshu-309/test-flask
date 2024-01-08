# import cv2
# import os
from PIL import Image
import io

# # Read the image as bytes
# image_content = b''
# with open('1.png', 'rb') as image_file:
#     image_content = image_file.read()
    

# class DetectFaceDemo:
#     def detectFace(self):
#         print("\nRunning DetectFaceDemo")

#         # Create a face detector from the cascade file
#         face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#         # Create an image file from the bytes
#         image_path = "temp_image.png"
#         with open(image_path, 'wb') as temp_file:
#             temp_file.write(image_content)

#         # Read the image
#         image = cv2.imread(image_path)

#         # Remove the temporary image file
#         os.remove(image_path)

#         if face_cascade.empty():
#             print("Face cascade not loaded")
#             return
#         if image is None or image.size == 0:
#             print("Failed to read image")
#             return

#         # Convert the image to grayscale
#         gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#         # Detect faces in the image
#         face_detections = face_cascade.detectMultiScale(
#             gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

#         print(f"Detected {len(face_detections)} faces") 
        
#         # crop the face
#         for (x, y, w, h) in face_detections:
#             # Crop the face
#             print("Cropping the image.....") 
#             face_image = image[y-40:y+h+40, x-40:x+w+40]
               
#                # Resize the face to 100x100
#             # print("Resizing the image.....")
#             resized_face = cv2.resize(face_image, (100, 100))
#             image_bytes = cv2.imencode(".png", resized_face)[1].tobytes()
#             # print(resized_face)
#             # print(image_bytes)

#                 # Save the resized face
#             print("Storing the image into output folder.....")
#             os.makedirs("faceDetected", exist_ok=True)
#             # print(f"Writing faceDetected")
#             cv2.imwrite("faceDetected/1.png", resized_face)
#             return image_bytes;

# def compress_image(image_content, target_size_kb=2, initial_quality=85): 
   
#     output_image = io.BytesIO(image_content)
    
#     original_image = Image.open(io.BytesIO(image_content)) 
 
#     while len(output_image.getvalue()) / 1024 > target_size_kb and initial_quality > 0:
#         output_image = io.BytesIO()  # Reset the BytesIO  
#         original_image.save(output_image, format="JPEG", quality=initial_quality)
#         initial_quality -= 5
#     return output_image.getvalue()
 
def printImg(byteInput):
    image = Image.open(io.BytesIO(byteInput))
    image.show()
    
# if __name__ == "__main__":
#     print("Hello, World!")
#     print("image cbytes " , len(image_content))
#     # print(len(compress_image()))
#     # image_content = compress_image
#     demo = DetectFaceDemo()
#     img = demo.detectFace()
#     print(len(img))
#     img = compress_image(img)
#     print(len(img))
#     printImg(img)


# import requests

# # Specify the URL where you want to send the POST request
# url = 'http://himanshu309.pythonanywhere.com/compress'

# # Replace 'your_image.jpg' with the path to your image file
# image_path = 'C:/Users/Himanshu/Downloads/python_API/python_API/faceDetected/1.png'

# # Open the image file and read its content
# files = {'files': ('image.png', open(image_path, 'rb'), 'image/png')}
# # Make the POST request
# response = requests.post(url, files=files)

# # Check the response
# if response.status_code == 200:
#     print("Image uploaded successfully!")
#     try:
#         # print(response.content)
#         printImg(response.content)
#     except ValueError:
#         print("Invalid JSON in response.")
#     # print(response)
# else:
#     print(f"Failed to upload image. Status code: {response.status_code}")
#     print(response.text)  # Print the response content for debugging purposes


import requests
import os
# Specify the URL where you want to send the POST request
url = 'http://himanshu309.pythonanywhere.com/compress'

# Replace 'your_image.jpg' with the path to your image file
image_path = 'C:/Users/Himanshu/Downloads/python_API/python_API/faceDetected/1.png'

# # Open the image file and read its content
# with open(image_path, 'rb') as image_file:
#     files = {'files': ('image.png', image_file, 'image/png')}
#     # Make the POST request
#     response = requests.post(url, files=files)

# Check if the file exists
if os.path.exists(image_path):
    # Open the file
    with open(image_path, 'rb') as image_file:
        files = {'files': ('image.png', image_file, 'image/png')}
        # Make the POST request
        response = requests.post(url, files=files)
else:
    print(f"Error: File not found - {image_path}")

# Check the response
if response.status_code == 200:
    print("Image uploaded successfully!")
    try:
        # Print the content length for debugging purposes
        print("Response content length:", len(response.content))
    except ValueError:
        print("Invalid JSON in response.")
else:
    print(f"Failed to upload image. Status code: {response.status_code}")
    print(response.text)  # Print the response content for debugging purposes
