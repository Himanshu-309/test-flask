 
from PIL import Image
import io

def compress_image(image_content, target_size_kb=2, initial_quality=85): 
    # read the image into bytes 
    image_byte = io.BytesIO(image_content)
    
    original_image = Image.open(io.BytesIO(image_content)) 
 
    # compress the image until sized is reduced to 2kb 
    while len(image_byte.getvalue()) / 1024 > target_size_kb and initial_quality > 0:
        image_byte = io.BytesIO()  # Reset the BytesIO  
        original_image.save(image_byte, format="JPEG", quality=initial_quality) #reduce the image quality 
        initial_quality -= 5 
        
    # return the image into bytes
    return image_byte.getvalue()