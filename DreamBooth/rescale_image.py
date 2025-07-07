from PIL import Image
import os

def resize_and_crop_images(folder_path, target_size=512): # default target size is 512

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if the file is an image
        if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Open the image
            image = Image.open(file_path)

            # Get the original width and height
            width, height = image.size

            # Calculate the new size while maintaining the aspect ratio
            if width <= height:
                new_width = target_size
                new_height = int(height * (target_size / width))
            else:
                new_width = int(width * (target_size / height))
                new_height = target_size

            # Resize the image
            resized_image = image.resize((new_width, new_height))

            left = (new_width - target_size) // 2
            top = (new_height - target_size) // 2
            right = (new_width + target_size) // 2
            bottom = (new_height + target_size) // 2

            # Perform the center crop
            cropped_image = resized_image.crop((left, top, right, bottom))
            cropped_image.save(file_path)


instance_image_path = "/instance/image/path/" # 替換成實例圖片的路徑
class_image_path = "/class/image/path/" # 替換成類別圖片的路徑

if len(os.listdir(instance_image_path)):
    resize_and_crop_images(instance_image_path)
    print("✅ Successfully rescale instance images")

if len(os.listdir(class_image_path)):
    resize_and_crop_images(class_image_path)
    print("✅ Successfully rescale class images")

