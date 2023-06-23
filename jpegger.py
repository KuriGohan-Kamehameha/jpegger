import os
from PIL import Image

def convert_to_jpg(input_folder):
    input_folder = os.path.expanduser(os.path.expandvars(input_folder))

    if not os.path.exists(input_folder):
        print("Input folder does not exist.")
        return

    image_formats = ['.png', '.jpeg', '.jpg', '.bmp', '.gif', '.webp']  # Supported image formats
    files_to_convert = []

    for filename in os.listdir(input_folder):
        if any(filename.lower().endswith(ext) for ext in image_formats):
            files_to_convert.append(filename)

    if not files_to_convert:
        print("No image files found in the specified folder.")
        return

    print("Files to be converted:")
    for filename in files_to_convert:
        print(filename)

    confirmation = input("Do you want to proceed with the conversion? (y/n): ")
    if confirmation.lower() != 'y':
        print("Conversion canceled.")
        return

    for filename in files_to_convert:
        try:
            image_path = os.path.join(input_folder, filename)
            image = Image.open(image_path)
            output_path = os.path.splitext(image_path)[0] + '.jpg'

            replace_confirmation = input(f"Do you want to replace {filename} with the converted JPEG file? (y/n): ")
            if replace_confirmation.lower() == 'y':
                image.save(output_path, 'JPEG')
                print(f"Converted {filename} to JPEG. Original image replaced.")
            else:
                print(f"Conversion of {filename} canceled.")

        except Exception as e:
            print(f"Error converting {filename}: {str(e)}")

# Interactive input
input_folder = input("Enter the path to the folder containing the images: ")

convert_to_jpg(input_folder)
