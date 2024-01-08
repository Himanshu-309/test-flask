# from flask import Flask, request, jsonify, send_file, Response
# import base64
# import sys
# import io
# sys.path.append('modules')
# import compress
# import faceDetection
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"

# @app.route("/compress", methods=['POST'])
# def compressImage():
#     # error = if file parameter not in url 
#     if 'files' not in request.files:
#         return jsonify({"error": "No file part !"})
#     image_File = request.files['files']

#     # error = if file not selected 
#     if image_File.filename == '':
#         return jsonify({"error": "No file selected !"})
#     # print("afd",len(image_File.read()))
#     # return jsonify({"er":""})
#     image_bytes = image_File.read()
#     print(len(image_bytes)) 
#     crop_image = faceDetection.detectFace(image_bytes)
#     # print("crop resut ", len(crop_image))
#     byte_compress_image = compress.compress_image(crop_image)
#     print("compress result ", len(byte_compress_image) )
    
#     # base64_compressed_image = base64.b64encode(byte_compress_image).decode('utf-8')
    
#     # Return the compressed image as a response
#     return Response(byte_compress_image, mimetype='application/octet-stream')
#     # return jsonify({"image" : base64_compressed_image})
#     # return send_file(io.BytesIO(crop_image),
#     #                  mimetype='image/jpg',
#     #                  as_attachment=True,
#     #                  download_name='compressed_image.jpg')

     


# if __name__ ==  "__main__":
#     app.run(debug=True)

from flask import Flask, request, jsonify, Response
import sys
import io
from PIL import Image
import base64

sys.path.append('modules')  # Assuming your modules are located in the 'modules' directory
import compress
import faceDetection

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/compress", methods=['POST'])
def compress_image():
    # Error if 'files' parameter is not in the request
    if 'files' not in request.files:
        return jsonify({"error": "No file part!"})

    image_file = request.files['files']

    # Error if no file is selected
    if image_file.filename == '':
        return jsonify({"error": "No file selected!"})

    # Read image bytes from the file
    image_bytes = image_file.read()

    # Detect faces in the image and get the cropped image
    crop_image = faceDetection.detectFace(image_bytes)

    # Compress the cropped image
    byte_compress_image = compress.compress_image(crop_image)

    # Return the compressed image as a response
    return Response(byte_compress_image, mimetype='application/octet-stream')

if __name__ == "__main__":
    # Bind to '0.0.0.0' and use port 5000 when running on PythonAnywhere
    app.run(host='0.0.0.0', port=5000, debug=True)
