import sys
from tkinter import image_names
import PIL
from PIL import Image
import io

def encrypt_image(image):
    gray_img = image.convert('L')  # Convert image to grayscale
    width, height = gray_img.size
    dotted_img = Image.new('L', (width, height))

    # Create a dotted grayscale image
    for x in range(0, width, 2):
        for y in range(0, height, 2):
            pixel_value = gray_img.getpixel((x, y))
            dotted_img.putpixel((x, y), pixel_value)

    return dotted_img

def decrypt_image(image):
    width, height = image.size
    original_img = Image.new('RGB', (width, height))

    # Convert dotted grayscale image back to original
    for x in range(0, width, 2):
        for y in range(0, height, 2):
            pixel_value = image.getpixel((x, y))
            original_img.putpixel((x, y), (pixel_value, pixel_value, pixel_value))

    return original_img
